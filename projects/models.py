from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    main_image = models.ImageField(upload_to='projects/')
    image1 = models.ImageField(upload_to='projects/')
    image2 = models.ImageField(upload_to='projects/')
    image3 = models.ImageField(upload_to='projects/')
    project_name = models.CharField(max_length=100)
    project_detail = models.TextField()
    project_category = models.CharField(max_length=100)
    project_date = models.DateField()
    project_url = models.URLField()
    def __str__(self):
        return self.project_name