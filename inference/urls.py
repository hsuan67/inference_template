from django.urls import path

from . import views

app_name = 'inference'
urlpatterns = [
    path("result", views.inference, name="submit"),
    path('test', views.test, name="test"),
]