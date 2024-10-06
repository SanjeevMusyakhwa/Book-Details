from django.shortcuts import render, redirect,get_object_or_404
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

def BookUpdate(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():
            form.save() 
            return redirect('bookList') 
    else:
        form = BookForm(instance=book) 

    return render(request, 'bookUpdate.html', {'form': form, 'book':book})