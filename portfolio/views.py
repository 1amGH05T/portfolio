from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, ContactMessage


# Create your views here.
def index(request):
    from .models import About

    about_info = About.objects.first()

    projects = Project.objects.order_by('-created_at')
    featured = projects.first() if projects.exists() else None

    return render(request, 'index.html', {
        'projects': projects,
        'featured': featured,
        'about_info': about_info,
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            messages.success(request, 'Thanks! Your message has been sent.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields before submitting.')

    return render(request, 'contact.html')

def detail(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        'project': project,
    }
    return render(request, 'details.html', context)

