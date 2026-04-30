from django.http import HttpResponse   # pyright: ignore[reportMissingModuleSource] # ✔️ CORRECT

from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]

# Create your views here.
#home page
def home(request):
    return render(request, "index.html")
#sign up page
def open_signup(request):
    return render(request, "signUp.html")
#sign in page
def open_signin(request):
    return render(request, "signIn.html")
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        address = request.POST.get('address')
        return HttpResponse("Signup successfully!")
    else:
        return HttpResponse("Invalid credentials")
        
