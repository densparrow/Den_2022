from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='home'),
      path('about_us', views.about, name='about_us'),
      path('my_page', views.my_page, name='my_page'),
      path('create', views.create, name='create'),
]