from django.contrib import admin
from django.urls import path

from Company import views
from Company.views import *

urlpatterns = [
    path('',views.inscription),
    path('clients/', views.clients, name="clients")

]
