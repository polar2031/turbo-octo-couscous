from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UrlView.as_view()),
    path('<str:id>', views.UrlView.as_view())
]
