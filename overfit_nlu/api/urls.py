from django.urls import path
from api.views.example_view import ExampleView
from api.views.nlp_api_view import NLPAPIView
app_name = 'api'

urlpatterns = [
    path('example', ExampleView.as_view(), name='example'),
    path('nlp_api', NLPAPIView.as_view(), name='nlp_api'),
]

