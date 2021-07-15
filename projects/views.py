from django.shortcuts import render

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'toprated': True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'toprated': True
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'toprated': False
    }
]


def projects(request):
    context = {"list_data": projectsList}
    return render(request, 'projects/projects.html', context=context)


def project(request, pk):
    project_objs = None
    for dt in projectsList:
        if dt.get('id') == str(pk):
            project_objs = dt
    return render(request, 'projects/project.html', context={'project_objs': project_objs})
