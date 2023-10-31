from django import forms
from .models import Readlist, Book

class AddBooksToReadlistForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Readlist
        fields = ['name', 'description', 'books']