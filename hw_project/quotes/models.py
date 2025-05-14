from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'
    
class Author(models.Model):
    fullname = models.CharField(max_length=50, unique=True)
    born_date = models.CharField(max_length=50, blank=True, null=True)
    born_location = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.fullname}'

class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    quote = models.TextField()

    def __str__(self):
        return f'{self.quote}'
    
class UserAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=50, blank=True)
    born_location = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} (added by {self.user.username})"

class UserQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.TextField()
    author = models.ForeignKey(UserAuthor, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Для модерації

    def __str__(self):
        return f"{self.quote[:50]}... (by {self.user.username})"