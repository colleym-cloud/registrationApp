from django.db import models
from django.contrib.auth.models import User, Group

class Module(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    credit = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    availability = models.BooleanField(default=True)
    courses_allowed = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date_of_registration = models.DateTimeField(auto_now_add=True)
