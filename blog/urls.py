#this folder is what django is directed to for further instructions for the different urls (pages on blog)

from django.urls import path
from . import views

# we are assigning a view called post list to the root url. this will match an empty string and the django url resolver
#will ignore the domain name that rpefixes the full url path. This tells django that views.post_list is the right place
#to go if someone enters the website at the 'http://127.0.0.1:8000/' address. We have named the url post list

urlpatterns = [
    path('', views.post_list, name= 'post_list'),
    path('post/<int:pk>/', views.post_detail, name= 'post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]