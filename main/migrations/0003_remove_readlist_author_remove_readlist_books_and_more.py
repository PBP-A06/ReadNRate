# Generated by Django 4.2.4 on 2023-10-31 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_book_description_book_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readlist',
            name='author',
        ),
        migrations.RemoveField(
            model_name='readlist',
            name='books',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Readlist',
        ),
    ]