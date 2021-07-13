from django.shortcuts import render, HttpResponse


def projects(request):
    return HttpResponse('This is out projects page.')


def project(request, pk):
    return HttpResponse(f'This is project page. Id send is : {pk}')
