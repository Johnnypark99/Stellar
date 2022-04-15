from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='drive-home'),
    path('favicon.ico', RedirectView.as_view(url='/static/drive/favicon.ico'), name='drive-fav-icon'),
    path('<path:str>', views.download, name='drive-download'),
]
