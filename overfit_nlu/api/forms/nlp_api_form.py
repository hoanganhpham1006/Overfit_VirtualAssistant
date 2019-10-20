from django import forms
from api.forms.abstract_form import AbstractForm

class NLPAPIForm(AbstractForm):
  message = forms.CharField()