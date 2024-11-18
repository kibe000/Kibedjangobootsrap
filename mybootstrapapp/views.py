from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def error(request):
    return render(request, '404.html')
def booking(request):
    return render(request, 'booking.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def contact(request):
    return render(request, 'contact.html')
def base(request):
    return render(request, 'base.html')