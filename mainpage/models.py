from typing import List
from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=350)
    background_photo = models.ImageField(upload_to='profile/')
    profile_photo = models.ImageField(upload_to='profile/')
    post = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skill = models.CharField(max_length=2500)
    about_me = models.TextField()
    services = models.TextField()
    complete_work = models.CharField(max_length=5)
    years_experiance = models.CharField(max_length=2)
    certificates = models.CharField(max_length=4)
    award_won = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    facebook = models.URLField()
    instagram = models.URLField()
    github = models.URLField()
    whatsapp = models.URLField()  

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Message From {self.name}'

class Certificate(models.Model):
    title = models.CharField(max_length=500)
    issuing_authority = models.CharField(max_length=500)
    certi_id = models.CharField(max_length=300)
    image = models.ImageField(upload_to='certificates/')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title