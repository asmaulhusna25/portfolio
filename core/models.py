from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/")

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/")

    def __str__(self) -> str:
        return self.title
