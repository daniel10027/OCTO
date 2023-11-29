from django.contrib import admin
from .models import Service, Team, Commentaires, Projet

# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'active', 'created', 'date_update')
    search_fields = ('titre', 'description')
    list_filter = ('active', 'created', 'date_update')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste', 'active', 'created', 'date_update')
    search_fields = ('nom', 'poste')
    list_filter = ('active', 'created', 'date_update')

@admin.register(Commentaires)
class CommentairesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'active', 'created', 'date_update')
    search_fields = ('nom', 'commentaire')
    list_filter = ('active', 'created', 'date_update')

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'client', 'active', 'created', 'date_update')
    search_fields = ('titre', 'categorie', 'client')
    list_filter = ('active', 'created', 'date_update')
