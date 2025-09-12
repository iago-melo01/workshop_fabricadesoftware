from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Cachorro
# Create your views here.
class Hello_view(View):
    def get(self, request):
        return HttpResponse("Boa tarde")
    
class CachorroListView(ListView):
    model = Cachorro
    template_name = 'list_dog.html'
    context_object_name = "cachorros"


