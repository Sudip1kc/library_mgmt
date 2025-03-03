from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Book, Member
from .forms import BookForm, MemberLoginForm, MemberRegistrationForm 

# Member Registration View
def member_register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('member_dashboard')
    else:
        form = MemberRegistrationForm()
    
    return render(request, 'library/member_register.html', {'form': form})


def member_login(request):
    if request.method == 'POST':
        form = MemberLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('member_dashboard')  
    else:
        form = MemberLoginForm()

    return render(request, 'library/member_login.html', {'form': form})

# Member Logout View
def member_logout(request):
    logout(request)
    return redirect('member_login')

# Member Dashboard (Protected)
@login_required
def member_dashboard(request):
    return render(request, 'library/member_dashboard.html')

# Admin Dashboard (Protected for Staff)
@staff_member_required
def admin_dashboard(request):
    return render(request, 'library/admin_dashboard.html')

#  Add Book View
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

#  Search Books
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'library/book_list.html', {'books': books})

def book_list(request):
    books = Book.objects.all().order_by('id')
    paginator = Paginator(books, 2)  # Show 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'library/book_list.html', {'page_obj': page_obj})


