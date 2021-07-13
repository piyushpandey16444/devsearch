from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return HttpResponse('This is out projects page.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects),
]
