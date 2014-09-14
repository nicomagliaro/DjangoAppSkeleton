from django.db import models
from django.contrib.auth.models import User


class userProfile(models.Model):

    """
        Este modelo extiende al usuario admin que viene por defecto en Django.
        Para usarlo es necesario instalar el modulo: Pillow
        cmd: "pip install pillow"
    """

    def url(self,filename):
        ruta = "media/MultimediaData/Users/%s/%s"%(self.user.username,filename)
        return ruta


    user        =   models.OneToOneField(User)
    photo       =   models.ImageField(upload_to=url)
    telefono    =   models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
