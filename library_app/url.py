from django.urls import path
from .import views

urlpatterns = [
  path('',views.librarian_login,name="librarian_login"),
  path('register/', views.librarian_register, name='librarian_register'),
  path('logout/',views.librarian_logout,name="librarian_logout"),
  path('add/',views.add_book,name='add_book'),
  path('show/',views.show_book,name='show_book'),
  # path('search/',views.book_list,name='book_list')
]