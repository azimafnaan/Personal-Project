from django.contrib import admin
from django.urls import path, include
from portfolio_core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('', include('portfolio_serv.urls')),
    path('', include('portfolio_edu.urls')),
]
