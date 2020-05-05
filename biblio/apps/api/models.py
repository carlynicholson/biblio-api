from django.db import models
from ..authentication.models import User


class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite, related_name='books', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    author = models.CharField()
    pages = models.IntegerField(default=0)
    published = models.IntegerField(max_length=4)
    description = models.TextField()
    is_favorite = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)

