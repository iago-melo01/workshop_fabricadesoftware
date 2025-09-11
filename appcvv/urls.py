from django.urls import path
from .views import Hello_view
urlpatterns = [
    path('', Hello_view.as_view(), name="index")
]