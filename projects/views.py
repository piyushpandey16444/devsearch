from django.shortcuts import render, HttpResponse


def projects(request):
    return render(request, 'projects.html')


def project(request, pk):
    return render(request, 'project.html')
