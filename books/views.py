from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Book

from django.contrib.auth.decorators import login_required

import json

# Create your views here.

@login_required(login_url='/admin/login')
def listbooks_view(request):
    listbooks = Book.objects.all()
    #return HttpResponse('OK')
    return render(request, 'books/listbook.html', {'listbooks': listbooks})

def books_view(request, author):
    book = get_object_or_404(Book, author__first_name=author)
    
    data = {
        'title': book.title,
        'order': book.order,
        'cover_image': " %s " % book.cover_image,
        'author': "%s %s" % (book.author.first_name, book.author.last_name),
        'editorial': {
            'name': book.editorial.name,
            'logo': " %s " % book.editorial.logo,
        }
    }   

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


from django.core import serializers
def books_serial_view(request):
    data = serializers.serialize("json", Book.objects.all())
    return HttpResponse(data, content_type='application/json')

from .forms import SumaForm
def suma_view(request):
    
    resultado = 0
    if request.method == "POST":
        form = SumaForm(request.POST) 
        if form.is_valid():
            valor1 = form.cleaned_data['valor1']
            valor2 = form.cleaned_data['valor2']
            valor3 = form.cleaned_data['valor3']

            resultado = float(valor1) + float(valor2)
    else:
        form = SumaForm()

    return render(request, 'books/suma.html', {"form":form, "resultado":resultado})


