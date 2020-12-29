from rest_framework import serializers
from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
  
  class Meta:
    fields = ('id', 'author', 'title', 'body', 'created_at',)
    model = Publication 
