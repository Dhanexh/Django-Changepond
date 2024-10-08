from rest_framework import serializers
from .models import bookmodel
from authorapp.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only = True)
    author = AuthorSerializer(read_only = True)
    class Meta:
        model = bookmodel
        fields = ['id','title','rating','author_id','author']
        read_only_fields=['id']