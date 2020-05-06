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

```PYTHON
class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    FICTION = 'FIC'
    NONFICTION = 'NON'
    GENRE_CHOICES = [
        (FICTION, 'Fiction'),
        (NONFICTION, 'Nonfiction'),
    ]
    genre = models.CharField(
        max_length=10,
        choices=GENRE_CHOICES,
        default='',
    )

    pages = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100, blank=True, default='')
    published = models.IntegerField()
    description = models.TextField()

    is_favorite = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
```

Example JSON output
```JSON
[
    {
        "id": 3,
        "title": "Dandelion Wine",
        "author": "Ray Bradbury",
        "owner": "founder",
        "genre": "Fiction",
        "pages": 239,
        "published": 1976,
        "publisher": "Spectra",
        "description": "In the unusual world of Green Town, Illinois, a twelve-year-old discovers the wonders of reality and the power of imagination during the summer of 1928.",
        "is_favorite": true,
        "is_public": true
    }
]
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

