from django.shortcuts import render, redirect
from books.models import Book



def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_date_view(request, date):
    template = 'books/books_list.html'
    date_list = list(Book.objects.values_list('pub_date', flat=True)
        .distinct().order_by('pub_date'))
    date_index = date_list.index(date)
    context = {
        'books': Book.objects.filter(pub_date=date)
    }
    context['prev_page'] = (
        date_list[date_index-1] if date_index != 0 else None
    )
    context['next_page'] = (
        date_list[date_index+1] if date_index != (len(date_list)-1) else None
    )

    return render(request, template, context)
