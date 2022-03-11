from django.urls import path
from . import views

urlpatterns = [
    path('isarps/<str:slug_isarp>', views.isarp , name="isarps"),
]