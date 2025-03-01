from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import MemberLoginForm
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'library/book_list.html', {'books': books})

def book_list(request):
    books = Book.objects.all()  # Get all books
    return render(request, 'library/book_list.html', {'books': books})


@login_required
def member_dashboard(request):
    return render(request, 'library/member_dashboard.html')

@staff_member_required
def admin_dashboard(request):
    return render(request, 'library/admin_dashboard.html')

def member_login(request):
    if request.method == 'POST':
        form = MemberLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the member dashboard or home page
    else:
        form = MemberLoginForm()

    return render(request, 'library/member_login.html', {'form': form})

def member_logout(request):
    logout(request)
    return redirect('login')
