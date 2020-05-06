## Biblio API

The API was created as a mini-project during my General Assembly Software Engineering Immersive cohort.

## Requirements
Build a simple Django restful API. Have at least 1 model with full CRUD functionality.

## Prerequisites
- Python 3.0
- PostgreSQL
- Django
- Django REST framework

## Code Snippet 
Implementation of Books model

```
class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, default='')
    pages = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100, blank=True, default='')
    published = models.IntegerField()
    description = models.TextField()
    is_favorite = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
```

## Package Installation
Before editing or running the application, use the following instructions:
1. Install virtual environment
    `virtualenv -p python3 myenv`
2. Activate virtual environment
    `source myenv/bin/activate`
3. Install Django, Django REST Framework, JSON Web Token Authentication for Django REST Framework
    `pip install django`
    `pip install djangorestframework`
    `pip install djangorestframework-jwt`
4. Install Psycopg2
    `pip install psycopg2`

