from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth.models import User

def librarian_register(request):
  if request.method=="POST":
    username = request.POST["username"]
    password = request.POST["password"]
    if User.objects.filter(username=username).exists():
      return render(request,'register.html',{'error':'username is alredy taken'})
    
    user=User.objects.create_user(username)
    user.set_password(password)
    user.is_active=False
    user.save()
    return render(request,"register.html",{"message":"registered! wait for admin approval."})
  return render(request,'register.html')

def librarian_login(request):
  if request.method=="POST":
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
      if user.is_active:
        login(request,user)
        return redirect('add_book')
    else:
      return render(request,'librarianLogin.html',{"error":"Invalid Credentials"})
  return render(request,'librarianLogin.html')

def librarian_logout(request):
  logout(request)
  return redirect("librarian_login")

@login_required(login_url='librarian_login')
def add_book(request):
  if request.method == "POST":
    book_id=request.POST["book_id"]
    title=request.POST["title"]
    author=request.POST["author"]
    Book.objects.create(book_id=book_id,title=title,author=author)
    return redirect("show_book")
  return render(request,"add_book.html")

@login_required(login_url='librarian_login')
def show_book(request):
  books=Book.objects.all().order_by('book_id')
  return render(request,'show_book.html',{'books':books})
# Create your views here.
