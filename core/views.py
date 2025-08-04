from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def about(request):
    return render(request, 'core/about.html')

def services_view(request):
    return render(request, 'core/services.html')

def contact(request):
    return render(request, 'core/contact.html')

def current_year(request):
    return {'now': datetime.now()}


from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm

def contact_view(request):
    form = ContactForm(request.POST or None)

    # Handle AJAX submission
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if form.is_valid():
            # You can handle form saving, email sending here
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    # Regular GET request or initial load
    return render(request, 'core/contact.html', {'form': form})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send auto response to user
            send_mail(
                subject="Thank you for contacting Prime Nurture",
                message=f"Hi {contact.name},\n\nThanks for reaching out. We have received your message and will get back to you shortly.\n\nWarm regards,\nPrime Nurture Team",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                fail_silently=False,
            )

            # Notify Admin (optional)
            send_mail(
                subject=f"New Contact Form Submission from {contact.name}",
                message=f"{contact.name} ({contact.email})\n\nPhone: {contact.phone}\nSubject: {contact.subject}\nMessage:\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
