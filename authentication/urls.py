from shop.views import *
from django.urls import path, include
from .views import *


urlpatterns = [
    path('log_in/', log_in, name='log_in'),
    path('register/', RegisterView.as_view(), name='register'),
    path('log_out/', log_out, name='log_out')
]
