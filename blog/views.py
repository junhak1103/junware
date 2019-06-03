from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html') 


def fakepage(request):
    return render(request, 'fakepage.html')

def help(request):
    return render(request, 'help.html')