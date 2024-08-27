from django.db import models

class City(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title}'

class Student(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.second_name[0]}.'




