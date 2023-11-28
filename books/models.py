from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    public_year = models.IntegerField(validators=[
        MinValueValidator(1000),
        MaxValueValidator(2023),
        ]
    )
    isbn = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('book', kwargs={'pk': self.pk})
    
    
class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    email = models.EmailField(verbose_name="Почта")
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name