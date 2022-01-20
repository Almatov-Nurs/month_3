from os import name
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class Raiting(models.Model):
    RATE_CHOICES = (
        (1, 'Bad'),
        (2, 'Okey'),
        (3, 'Fine'),
        (4, 'Good'),
        (5, 'Amaizing'),
    )

    rait = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    raiting = models.PositiveSmallIntegerField(choices=RATE_CHOICES)