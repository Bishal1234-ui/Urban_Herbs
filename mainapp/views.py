from django.shortcuts import render

# Create your views here.
def LoginPage(request): 
    return render(request, 'mainapp/login.html')

# page 2 - Learn vs Shop
def page2(request):
    return render(request, 'mainapp/page2.html')

# e learn home
def ehome(request):
    return render(request,'mainapp/learn/home.html')

# pricing of e learn
def pricing(request):
    return render(request, 'mainapp/learn/price.html')


# shop page
def shop(request):
    return render(request, 'mainapp/shop/shop.html')