from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('clubs/', views.clubs, name='clubs'),  # Clubs page
    path('club/<int:club_id>/', views.club_detail, name='club_detail'),  # Club detail page
    path('services/', views.services, name='services'), #for services
    path('contact/', views.contact, name='contact'),  # Add this line for Contact
    path('contact/submit/', views.contact_submit, name='contact_submit')
]


