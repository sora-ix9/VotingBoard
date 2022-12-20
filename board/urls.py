from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home'),
    path('admin/', admin.site.urls),
]