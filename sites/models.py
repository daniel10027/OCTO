from django.db import models
from tinymce.models import HTMLField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.urls import reverse

# Create your models here.
class Service(models.Model):
    """Model definition for Service."""
    titre = models.CharField(max_length=150)
    description = HTMLField()
    big_description = HTMLField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        return self.titre

    def get_absolute_url(self):
        """Return absolute url for Service."""
        return ('')

    # TODO: Define custom methods here
    
class Team(models.Model):
    nom = models.CharField(max_length=150)
    poste = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="team/photo")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    """Model definition for Team."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Team."""

        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        """Unicode representation of Team."""
        return self.nom


    def get_absolute_url(self):
        """Return absolute url for Team."""
        return ('')

    # TODO: Define custom methods here
    
    def save(self):
        """Save method for ImageProduit."""
        im = Image.open(self.photo)
        output = BytesIO()
        im = im.resize( (353,307) )
        im.save(output, format='PNG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.png" %self.photo.name.split('.')[0], 'image/png', sys.getsizeof(output), None)
        super(Team,self).save()

class Commentaires(models.Model):
    """Model definition for Commentaires."""
    nom = models.CharField(max_length=50)
    commentaire = HTMLField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Commentaires."""

        verbose_name = 'Commentaires'
        verbose_name_plural = 'Commentairess'

    def __str__(self):
        """Unicode representation of Commentaires."""
        return self.nom


    def get_absolute_url(self):
        """Return absolute url for Commentaires."""
        return ('')

    # TODO: Define custom methods here


class Projet(models.Model):
    """Model definition for Projet."""
    titre = models.CharField(max_length=150)
    categorie = models.CharField(max_length=150)
    annee = models.CharField(max_length=150)
    client = models.CharField(max_length=150)
    description = HTMLField()
    image = models.ImageField(upload_to="projets/images")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for Projet."""

        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        """Unicode representation of Projet."""
        return self.titre


    def get_absolute_url(self):
        """Return absolute url for Projet."""
        return ('')

    # TODO: Define custom methods here
