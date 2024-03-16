from django.urls import path

from joke.views import TestView

urlpatterns = [
    path("", TestView.as_view())
]
