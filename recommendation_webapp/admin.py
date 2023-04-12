#The admin.py file is used to display your models in the Django admin panel. 
# You can also customize your admin panel

from django.contrib import admin
from .models import Movie, Book, Anime2

admin.site.register(Movie)
admin.site.register(Book)
admin.site.register(Anime2)
