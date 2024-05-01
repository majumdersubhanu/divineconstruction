from django.shortcuts import render
from app.models import UpcomingProjects, Testimonial, Project
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuoteForm
from .models import UpcomingProjects, Testimonial, Project

from django.shortcuts import render
from django.http import HttpResponse
from .models import UpcomingProjects, Testimonial, Project, Quote


def index(request):
    if request.method == 'POST':
        # Manually retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Simple validation
        if name and email and phone and message:
            Quote.objects.create(name=name, email=email, phone=phone, message=message)
            return JsonResponse(
                {'status': 'success', 'message': 'Your request has been registered successfully. Thank you!'})
        else:
            # Respond with an error if any fields are missing
            return JsonResponse({'status': 'error', 'message': 'Please fill all the fields.'}, status=400)

    # Initial GET request to load page
    upcoming_projects = UpcomingProjects.objects.all()
    testimonials = Testimonial.objects.all()
    recent_projects = Project.objects.all().order_by('-name')[:5]

    context = {
        'upcoming_projects': upcoming_projects,
        'testimonials': testimonials,
        'recent_projects': recent_projects,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'index.html')
