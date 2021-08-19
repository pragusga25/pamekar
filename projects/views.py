from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(request):
    msg = 'Hello World'
    age = 30
    context = {'msg': msg, 'age': age}
    return render(request, 'projects/projects.html', context)

def project(request):
    return render(request,'projects/single-project.html')
