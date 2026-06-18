from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    ROLE_CHOICES = [
        ('Employer', 'Employer'),
        ('Candidate', 'Candidate')
    ]

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_description = models.TextField()
    company_website = models.URLField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resume/')
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.full_name

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # company = models.CharField(max_length=100, default="Unknown Company")
    location = models.CharField(max_length=100)
    salary = models. DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate} - {self.job}"