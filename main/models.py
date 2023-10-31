from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     publication_date = models.DateField(null=True, blank=True)
#     genre = models.CharField(max_length=50, blank=True)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

# class Readlist(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField()
#     books = models.ManyToManyField(Book, blank=True)
 
#     def __str__(self):
#         return self.title