from django.urls import path
from .views import test_api_view

urlpatterns = [
    path("api/hello", test_api_view),
]

