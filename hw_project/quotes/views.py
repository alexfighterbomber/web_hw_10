from django.shortcuts import render
from django.core.paginator import Paginator
from utils.utils import get_mongo_db

def main(request, page=1):
    db = get_mongo_db()
    quotes = db.quote.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "index.html", context={'quotes': quotes_on_page})