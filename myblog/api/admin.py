from django.contrib import admin
from .models import Articles
from .models import Genre
# Register your models here.

admin.site.register(Articles)
admin.site.register(Genre)