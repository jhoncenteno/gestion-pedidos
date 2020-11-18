from django.shortcuts import render

def home(request):

    return render(request, 'Ahome.html')


def base(request):

    return render(request, '0base.html')