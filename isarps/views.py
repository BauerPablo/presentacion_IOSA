from django.shortcuts import render
from isarps.models import Isarp

# Create your views here.
def isarp(request, slug_isarp):

    isarp = Isarp.objects.get(slug_isarp=slug_isarp)

    return render(request, 'isarps/isarp.html', {
        'isarp': isarp
    })

