from django.urls import path
from . import views

app_name="portscanner"
urlpatterns = [
    path('', views.home, name="home"),
    path('scan/', views.scan, name="scan"),
]
