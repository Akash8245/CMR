from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils.timezone import now

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True, default=0)  
    branch = models.CharField(max_length=100, null=True, blank=True, default="")  

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Teacher(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)

    def is_upcoming(self):
        return self.date >= now()

    def __str__(self):
        return self.title
    
class Review(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.review_text[:30]}"