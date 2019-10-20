from django.urls import path
from . import views

urlpatterns = [
  path("speech_to_text", views.speech_to_text, name="speech_to_text"),
]