from django.contrib import admin

from cats.models import Breed, Cat

# Register your models here.

admin.site.register(Breed)
admin.site.register(Cat)
