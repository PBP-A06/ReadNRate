from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    number_of_reviews = models.IntegerField(null=True, blank=True)
    book_description = models.TextField(null=True, blank=True)
    image_link = models.TextField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
<<<<<<< HEAD
        return self.title
=======
        return self.title
>>>>>>> ac7699fb7ad89aee271404973718fe1658eaed1d
