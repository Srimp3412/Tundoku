from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BookModel

def index_view(request):
    object_list = BookModel.objects.all()
    count = BookModel.objects.count()
    return render(request, 'book/index.html', {'object_list': object_list, 'count':count})

def logout_view(request):
    logout(request)
    return redirect('index')

class BookList(ListView):
    template_name = 'book/book_list.html'
    model = BookModel

class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model = BookModel

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model = BookModel
    fields = {'title', 'isbn', 'author', 'description', 'book_img'}
    success_url = reverse_lazy('book-list')

class DeleteBookView(DeleteView):
    template_name = 'book/book_delete.html'
    model = BookModel
    success_url = reverse_lazy('book-list')

class UpdateBookView(UpdateView):
    model = BookModel
    fields = {'title', 'isbn', 'author', 'description', 'book_img'}
    template_name = 'book/book_update.html'
    success_url = reverse_lazy('book-list')


