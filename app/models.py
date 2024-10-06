from django.db import models


class Author(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
  
class Book(models.Model):
  name = models.CharField(max_length=200)
  author = models.ForeignKey('Author', on_delete=models.CASCADE)
  admin = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
  isbn = models.CharField(max_length=12)
  published_date = models.DateField()
  price = models.IntegerField()

  def __str__(self):
    return self.name