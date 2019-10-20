from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from api.forms.nlp_api_form import NLPAPIForm
from api.helpers.nlp_api_helper import processing
from api.helpers.response_format import json_format

class NLPAPIView(APIView):
    parser_classes = (MultiPartParser,)
    success = 'Request Success'
    failure = 'Request Failed'

    def post(self, request):
        form = NLPAPIForm(request.POST,)
        if not form.is_valid():
            return JsonResponse(form.errors, status=422)
        message = form.cleaned_data.get('message')
        return self._format_response(message)
    
    def _format_response(self, message):
        result = processing(message)
        return json_format(code=200, message=self.success, data=result, errors=None)
  