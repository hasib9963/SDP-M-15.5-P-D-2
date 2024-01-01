
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('musicians/',include('musicians.urls')),
    path('albums/',include('albums.urls')),
    
]
