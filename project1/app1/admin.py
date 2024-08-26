from django.contrib import admin

# Register your models here.
from .models import Author,Posts,Comment

admin.site.register(Author)
admin.site.register(Posts)
admin.site.register(Comment)