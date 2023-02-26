"""lightCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crm.views import FirstView, SecondView, ThirdView,ContactView, ContactViewID
from app.views import main_route
urlpatterns = [
    path('', main_route.as_view()),
    path('admin/', admin.site.urls),
    # We associate our view class with a particular endpoint
    path("first/", FirstView.as_view()),
    path("second/<param>/", SecondView.as_view()),
    path("third/", ThirdView.as_view()),
    path("contact/", ContactView.as_view()),
    path('contact/<id>/', ContactViewID.as_view()),

    
]
