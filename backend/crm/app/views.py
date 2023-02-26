from django.shortcuts import render

# Create your views here.
def main_route (request):
    render(request, "index.html")