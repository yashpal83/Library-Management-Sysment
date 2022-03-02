from django.shortcuts import redirect, render, HttpResponse
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class SignupView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = "/"
    success_message = "Your account has been created successfully."


def home(request):
    return render(request, "home.html")

def handlelogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully logged-in.")
            allbook = Book.objects.all()
            return render(request, "adminpage.html", {'allbook':allbook})
            
        else:
            messages.warning(request, "Bad Credentials, try again.")
            return redirect("/login")

    return render(request, "login.html")


def addbook(request):
    if request.method == 'POST':
        bookname = request.POST['bookname']
        author = request.POST['author']
        isbn = request.POST['isbn']
        quantity = request.POST['quantity']

        book = Book(book_name = bookname, author = author, isbn = isbn, quantity= quantity)

        book.save()
        return redirect("/adminpage")
    
    return HttpResponse("Error : 404")


def adminpage(request):
    allbook = Book.objects.all()
    return render(request, "adminpage.html", {'allbook':allbook})



def update(request, sno):
    if request.method == "POST":
        bookname = request.POST['bookname']
        author = request.POST['author']
        isbn = request.POST['isbn']
        quantity = request.POST['quantity']

        book = Book.objects.get(sno = sno)
        book.book_name = bookname
        book.author = author
        book.isbn = isbn
        book.quantity = quantity
        book.save()
        return redirect("/adminpage")
        
    book = Book.objects.get(sno = sno)
    return render(request, "update.html", {'book': book})

def delete(request, sno):
    book = Book.objects.get(sno = sno)
    book.delete()
    return redirect("/adminpage")

def studentpage(request):
    allbook = Book.objects.all()
    return render(request, "studentpage.html", {'allbook':allbook})


def handlelogout(request):
    logout(request)
    messages.success(request, "You are successfully Logged Out.")
    return redirect("/")
