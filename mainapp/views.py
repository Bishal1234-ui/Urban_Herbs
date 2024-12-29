from django.shortcuts import render

# Create your views here.
def LoginPage(request): 
    return render(request, 'mainapp/login.html')

# page 2 - Learn vs Shop
def page2(request):
    return render(request, 'mainapp/page2.html')