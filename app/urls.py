from django.urls import path
from app import views
urlpatterns = [
    path('', views.bookList, name='bookList'),
    path('bookCreate/', views.bookCreate, name='bookCreate'),
    path('bookDelete/<int:pk>/', views.bookDelete, name='bookDelete'),
    path('bookUpdate/<int:pk>/', views.BookUpdate, name='bookUpdate'),
]
