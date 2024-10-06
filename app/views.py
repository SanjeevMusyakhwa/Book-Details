from django.shortcuts import render, redirect
from app.models import Book
from app.forms import BookForm
# Create your views here.

def bookList(request):
  books = Book.objects.all()
  return render(
    request,
    'bookList.html',
    {'books': books}
  )


def bookCreate(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('bookList')
  else:
    form = BookForm()
    print("Hello")
  return render(
    request, 'bookcreate.html', {'form': form}
  )

def bookDelete(request,pk):
  book = Book.objects.get(id =pk)
  book.delete()
  return redirect('bookList')