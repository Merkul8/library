from django.contrib import admin
from .models import Book, Person

# Регистрация моделей в админке
admin.site.register(Book)
admin.site.register(Person)
