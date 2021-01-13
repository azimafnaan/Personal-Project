from django.shortcuts import render

# Create your views here.
def skill(request):
    return render(request, 'portfolio_edu/skill.html')