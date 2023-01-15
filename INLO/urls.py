from django.contrib import admin
from django.urls import path

from Company.views import clients, inscription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', clients),
    path('signup/', inscription)

]
