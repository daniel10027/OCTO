from django.shortcuts import render
from .models import *
# Create your views here.
def Error404(request):
    return render(request,'404.html')

def index(request):
    context = {
        'services' : Service.objects.all().order_by('titre'),
        'teams' : Team.objects.all().order_by('nom'),
        'commentaires' : Commentaires.objects.all().order_by('nom'),
    }
    return render(request,'index.html', context=context)

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

def development(request):
    return render(request,'development.html')

def marketing(request):
    return render(request,'digital-marketing.html')

def design(request):
    return render(request,'graphic-design.html')

def pricing(request):
    return render(request,'pricing.html')

def projects(request):
    return render(request,'projects.html')

def projectsDetails(request):
    return render(request,'projects-details.html')

def seo(request):
    return render(request,'seo-marketing.html')

def services(request):
    return render(request,'services.html')

def servicesDetails(request):
    return render(request,'service-details.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')


def uiux(request):
    return render(request,'ui-ux-design.html')


    