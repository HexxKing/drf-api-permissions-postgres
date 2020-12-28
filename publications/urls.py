from django.urls import path
from .views import PublicationList, PublicationDetail

urlpatterns = [
  path('<int:pk>/', PublicationDetail.as_view()),
  path('', PublicationList.as_view()),
]
