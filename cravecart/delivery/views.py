from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]

# Create your views here.
def home(request):
    return render(request, "index.html")
