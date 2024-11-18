from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('booking/',views.booking,name='my_booking'),
    path('contact/',views.contact,name='my_contact'),
    path('team/',views.team,name='my_team'),
    path('service/',views.service,name='my_service'),
    path('testimonial/',views.testimonial,name='my_testimonial'),
    path('error/',views.error,name='my_error')

]

