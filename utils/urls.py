from django.urls import path
from .views import IndexView

urlpatterns = [
    path('begin/', IndexView.as_view(), name='Begin'),
]
