from django.urls import path
from . import views
urlpatterns = [
    path('', views.Hello_view.as_view(), name="index"),
    path('listarcachorros/', views.CachorroListView.as_view(), name='listar_cachorros' )
]