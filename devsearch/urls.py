from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return HttpResponse('This is out projects page.')

def project(request, pk):
    return HttpResponse(f'This is project page. Id send is : {pk}')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects),
    path('project/<str:pk>/', project),
]
