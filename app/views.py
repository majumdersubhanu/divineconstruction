from django.http import JsonResponse
from django.shortcuts import render

from .models import AssociatePartner, UpcomingProjects, Testimonial, Project, Quote, Enquiry, TeamMember


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
    associates = AssociatePartner.objects.all()
    recent_projects = Project.objects.all().order_by('-name')[:5]

    context = {
        'upcoming_projects': upcoming_projects,
        'testimonials': testimonials,
        'recent_projects': recent_projects,
        'associates': associates,
    }
    return render(request, 'index.html', context)


def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about.html', context={'team_members': team_members})


def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'projects.html', context)


def contact(request):
    if request.method == 'POST':
        # Manually retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Simple validation
        if name and email and subject and message:
            Enquiry.objects.create(name=name, email=email, subject=subject, message=message)
            return JsonResponse(
                {'status': 'success', 'message': 'Your request has been registered successfully. Thank you!'})
        else:
            # Respond with an error if any fields are missing
            return JsonResponse({'status': 'error', 'message': 'Please fill all the fields.'}, status=400)

    return render(request, 'contact.html')


def project_detail(request, project_id):
    project = Project.objects.all().filter(id=project_id).first()
    context = {
        'project': project
    }

    return render(request, 'project-details.html', context)


def upcoming_project_detail(request, project_id):
    project = UpcomingProjects.objects.all().filter(id=project_id).first()
    context = {
        'project': project
    }

    return render(request, 'project-details.html', context)
