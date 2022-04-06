from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='drive-home'),
    path('<path:str>', views.download, name='drive-download'),
]
