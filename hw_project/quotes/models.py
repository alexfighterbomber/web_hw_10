from django.db import models

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