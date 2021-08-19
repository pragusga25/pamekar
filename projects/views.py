from django.shortcuts import render
from django.http import HttpResponse

projectList = [
{'id':1, 'title': 'Compfest13', 'description': 'Awesome WebApp'},
{'id':2, 'title': 'BETIS2020', 'description': 'Responsive web'},
{'id':3, 'title': 'Mentoring', 'description': 'Mentoring Website'},
]

# Create your views here.
def projects(request):
    msg = 'Hello World'
    age = 30
    context = {'msg': msg, 'age': age, 'projectList':projectList}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    context = {'project':projectObj}
    return render(request,'projects/single-project.html', context)
