from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Remigiusz",
        "title": "Blog Post1",
        "content": "First Post coctent",
        "date_posted": "24.07.2022",
    },
    {
        "author": "Wojewodzki",
        "title": "Blog Post2",
        "content": "Second Post coctent",
        "date_posted": "24.07.2022",
    },
]


def home(request):
    context ={
        "post": posts
    }
    return render(request=request, template_name='blog/home.html', context=context)

def abotu(request):
    return HttpResponse('<h1>About</h1>')
