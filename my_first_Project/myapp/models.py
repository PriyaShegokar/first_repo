from django.db import models
from django.db.models.fields.related import ForeignKey

# employee,department,customer,order,

# Create your models here.

class Auther(models.Model):
    auther_id = models.IntegerField(primary_key=True)
    auther_name = models.CharField(max_length=20,null=True)
    class Meta:
        db_table = "auther"
    def __str__(self):
        return self.auther_name


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    auther_id = models.ForeignKey('Auther', on_delete = models.CASCADE, related_name="auther_table1")
    book_name = models.CharField(max_length=20,null=True)
    class Meta:
        db_table = "book"
    def __str__(self):
        return self.book_name


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=20)
    book = models.ManyToManyField(Book)
    class Meta:
        db_table = "store"
    def __str__(self):
        return self.store_name

# =======================================================================




