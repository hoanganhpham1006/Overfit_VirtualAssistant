from django.shortcuts import render, redirect
from projects.models import *
from django.http import StreamingHttpResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .forms import RegisterForm, UploadCvForm

# Create your views here.

def speech_to_text(request):
  context = {

  }
  return render(request, 'speech_to_text.html', context)
