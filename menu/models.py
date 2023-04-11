from django.db import models

# Create your models here.

class MenuType(models.Model):
    name = models.CharField(max_length = 1000)
    description = models.CharField(max_length = 100000, default = None)
    image = models.ImageField(upload_to = 'menu type/', default = 'menu type/dish-2.png')

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length = 1000)
    price = models.IntegerField()
    description = models.CharField(max_length = 10000000, default = None)
    type = models.ForeignKey(MenuType, on_delete = models.CASCADE, blank = True, null = True, default = None)
    image = models.ImageField(upload_to = 'menu item/', default = 'menu item/dish-3.png')

    def __str__(self):
        return self.name
