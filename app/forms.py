from django import forms
from app.models import Book

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['name', 'author','isbn','published_date', 'price']