from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.member_register, name='member_register'),  
    path('login/', views.member_login, name='member_login'),
    path('logout/', views.member_logout, name='member_logout'),
    path('member-dashboard/', views.member_dashboard, name='member_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('book_list/', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('search/', views.search_books, name='search_books'),
]
