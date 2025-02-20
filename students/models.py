from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    age = models.IntegerField()
    guruh = models.IntegerField()
    kurslar = [
        ("Back-End", "Back-End"),
        ("Front-End", "Front-End"),
        ("Design", "Design")

    ]
    kurs = models.CharField(max_length=15, choices=kurslar)