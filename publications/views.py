from rest_framework import generics
from .models import Publication
from .permissions import IsAuthorOrReadOnly
from .serializers import PublicationSerializer

class PublicationList(generics.ListCreateAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationSerializer

class PublicationDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Publication.objects.all()
  serializer_class = PublicationSerializer
