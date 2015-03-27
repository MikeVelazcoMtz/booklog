from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/admin/login')
def listbooks_view(request):
    listbooks = Book.objects.all()
    #return HttpResponse('OK')
    return render(request, 'books/listbook.html', {'listbooks': listbooks})
