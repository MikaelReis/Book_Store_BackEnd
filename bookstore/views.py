from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render  # Use render em vez de loader

import git


@csrf_exempt
def update(request):
    if request.method == "POST":
        """
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        """
        repo = git.Repo("/home/MikaelReis/bookstore")
        origin = repo.remotes.origin

        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


def hello_world(request):
    return render(request, 'hello_world.html')

def home_view(request):
    """View para a página inicial"""
    return render(request, 'home.html')

def home_page(request):
    return render(request, 'home.html')