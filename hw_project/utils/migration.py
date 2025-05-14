import os, sys
from pathlib import Path

project_root = Path(__file__).parent.parent 
sys.path.append(str(project_root))

from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
import django
django.setup()

from quotes.models import Author, Quote, Tag
from utils import get_mongo_db

db = get_mongo_db()
authors = db.author.find()
quotes = db.quote.find()
for author in authors:
    Author.objects.get_or_create(
        fullname=author.get('fullname'),
        born_date=author.get('born_date'),
        born_location=author.get('born_location'),
        description=author.get('description')
    )

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))
    if not exist_quote:
        author = db.author.find_one({"_id": quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag) 