from django.shortcuts import render
from app_blog.models import Categorias, post

def blog(request):

    posts = post.objects.all()
    
    return render(request, 'Dblog.html', {'posts' : posts})


def nacionales(request):

    lista_nacionales = post.objects.filter(categorias__nombre="Nacionales")

    return render (request, 'D.1nacionales.html', {'lista_nacionales' : lista_nacionales})

def internacionales(request):

    lista_internacionales = post.objects.filter(categorias__nombre="Internacionales")

    return render (request, 'D.2internacionales.html', {'lista_internacionales' : lista_internacionales})
    
