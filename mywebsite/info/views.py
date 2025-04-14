from django.shortcuts import render, get_object_or_404 , redirect
from .models import Club, ClubImage ,ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    featured_clubs = Club.objects.filter(name__in=["Zero1Coded", "Lightblenders", "Literary Committee"])  # Display 3 featured clubs
    clubs = Club.objects.all()  # Fetch all clubs
    gallery_images = ClubImage.objects.all()  # Fetch all gallery images

    return render(request, 'info/home.html', {
        'featured_clubs': featured_clubs,
        'clubs': clubs,
        'gallery_images': gallery_images,
    })

def about(request):
    return render(request, 'info/about.html')

def clubs(request):
    all_clubs = Club.objects.all()  # Get all clubs from the database
    return render(request, 'info/clubs.html', {'all_clubs': all_clubs})

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    gallery_images = club.gallery.all()  # Fetch all gallery images for the club
    return render(request, 'info/club_detail.html', {'club': club, 'gallery_images': gallery_images})

def services(request):
    return render(request, 'info/services.html')

def contact(request):
    return render(request, 'info/contact.html')

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Your message has been received! We will get back to you soon.')
        # Process the data (send email or save to database)
        return redirect('contact')  # Create this view/URL
    return redirect('contact')


