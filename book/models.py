from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    number_of_reviews = models.IntegerField(null=True, blank=True)
    book_description = models.TextField(null=True, blank=True)
    image_link = models.TextField(null=True, blank=True)
<<<<<<< HEAD
    stars = models.IntegerField(null=True, blank=True)
=======
    stars = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
>>>>>>> 62b9ac142c6926e1adac08f874bbd8050920f02d
