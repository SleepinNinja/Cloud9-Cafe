from django.db import models
from django.contrib.auth.models import User


# Create your models here.

"""
Here by default the values are set to not null,
ie. a code like this will generate a table creation like this
in sqlite
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
"""

class Image(models.Model):
    page = models.CharField(max_length = 10000)
    section = models.CharField(max_length = 10000, null = True)
    image = models.ImageField(upload_to = 'img/')

    def __str__(self):
        return self.page + ' ' + self.section


class Text(models.Model):
    page = models.CharField(max_length = 10000, default = "")
    section = models.CharField(max_length = 10000, default = "")
    title = models.CharField(max_length = 1000, blank = True, default = "")
    content = models.TextField(blank = True, default = "")

    def __str__(self):
        return self.page + ' ' + self.section + ' ' + self.title


class ProfilePhoto(models.Model):
    profile_photo = models.ImageField(upload_to = 'media/profile_img' , default = 'profile_img/woman.png')
    user = models.OneToOneField(User, on_delete = models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.TextField();
