from django import forms
from book.models import Book
from .views import *

books = Book.objects.all().order_by('title')
TITLE_CHOICES = []
for i in range(100):
    book = books[i]
    TITLE_CHOICES.append(tuple([i+1, book.title]))
    
class SearchForm(forms.Form):
    search = forms.ModelChoiceField(
        label='Choose a particular book ranked by Rating on leaderboard:',
        queryset=Book.objects.all(),
        widget=forms.Select(),
        help_text=TITLE_CHOICES
    )
