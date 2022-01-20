from os import name
from statistics import mode
from webbrowser import get
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from .models import Raiting

def book_all(request):
    post = models.Book.objects.all()
    return render(request, "book_list.html", {'post': post})

def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    rate = Raiting.objects.filter()
    return render(request, 'book_detail.html', {'book': book,'rate':rate})

def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('You add new book!')
    else:
        form = forms.BookForm()
    return render(request, "add_book.html", {"form": form})

def book_update(request, id):
    book_obj = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_obj, data=request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('book updated succefully')
            return redirect(reverse("book:book_all"))
    else:
        form = forms.BookForm(instance=book_obj)
    return render(request, 'book_update.html', {"form":form,'object': book_obj})

def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse('Book Deleted')

def book_raiting(request, id):
    method = request.method
    if method == "POST":
        form = forms.RaitingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('book:book_all'))
    else:
        form = forms.RaitingForm()
    return render(request, "book_raiting.html", {"form": form})