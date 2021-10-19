from django.contrib import admin
from .models import Book,Store,Auther

# Register your models here.
myModels = [Book,Store,Auther]  # iterable list
admin.site.register(myModels)