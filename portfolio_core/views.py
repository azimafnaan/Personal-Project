from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio_core/home.html')


def contact(request):
    return render(request, 'portfolio_core/contact.html')   