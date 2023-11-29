from django.urls import path
from .views import *

urlpatterns = [
    # Existing paths
    path('', index, name="index"),
    # Add these paths
    path('404/', Error404, name="error404"),
    path('about/', about, name="about"),
   
    path('contact/', contact, name="contact"),
    path('development/', development, name="development"),
    path('digital-marketing/', marketing, name="digital_marketing"),
    path('graphic-design/', design, name="graphic_design"),
    path('pricing/', pricing, name="pricing"),
    path('projects/', projects, name="projects"),
    path('projects-details/', projectsDetails, name="projects_details"),
    path('seo-marketing/', seo, name="seo_marketing"),
    path('services/', services, name="services"),
    path('services-details/', servicesDetails, name="services_details"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('ui-ux-design/', uiux, name="ui_ux_design"),
]
