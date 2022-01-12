from django.shortcuts import render, get_object_or_404
from . import models

def book_all(request):
    post = models.Book.objects.all()
    return render(request, "post_list.html", {'post': post})

def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book': book})
