from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('books/', BookAPIList.as_view(), name='library'),
    path('books/<int:pk>/', BookAPIDetail.as_view(), name='book')
]