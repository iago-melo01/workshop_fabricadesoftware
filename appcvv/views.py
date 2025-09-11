from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Hello_view(View):
    def get(self, request):
        return HttpResponse("Boa tarde")