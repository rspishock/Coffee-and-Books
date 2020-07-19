from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=75)
    isbn = models.CharField(max_length=25)
    genre = models.CharField(max_length=25, default='Genre')
    review = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='reviews/images/')
    url = models.URLField(blank=True)
