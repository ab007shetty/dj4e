from django.db import models

class States(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200)
    justification = models.TextField(default="")
    year = models.IntegerField(default=0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    area_hectares = models.FloatField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey('Iso', on_delete=models.CASCADE, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)
    states = models.ForeignKey('States', on_delete=models.CASCADE, null=True)


    def __str__(self) :
        return self.name





