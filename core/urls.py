from django.urls import path,include
from .views import Home, index
urlpatterns = [
path('',Home.as_view(), name='home')
    
]
