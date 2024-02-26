from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    date_of_joining = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    compensation = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.person.name} (Teacher)"

class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.person.name} (Student)"

class Club(models.Model):
    club_name = models.CharField(max_length=100)

    def __str__(self):
        return self.club_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"
