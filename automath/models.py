from _ast import mod

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Question(models.Model):
    """
    Modèle de question
    """

    class Themes(models.TextChoices):
        "Liste des thèmes accessibles"
        ENTIERS = 'ENT', _('Entiers')
        DECIMAUX = 'DEC', _('Démimaux')
        RELATIFS = 'REL', _('Relatifs')
        FRACTIONS = 'FRA', _('Fractions')

    class Niveaux(models.TextChoices):
        "Liste des niveaux proposés"
        SIXIEME = "6eme", _('Sixième')
        CINQUIEME = "5eme", _('Cinquième')
        QUATRIEME = "4eme", _('Quatrième')
        TROISIEME = "3eme", _('Troisième')
        SECONDE = "2nde", _('Seconde')
        PREMIERE = "1ere", _('Première')
        TERMINALE = "Term", _('Terminale')



    titre = models.CharField(max_length=200, primary_key=True)
    question = models.TextField(null=True)
    theme = models.CharField(max_length=3, choices=Themes.choices)
    enonce = models.TextField(null=False)
    niveau = models.CharField(max_length=4,choices=Niveaux.choices)

    def __str__(self):
        return self.titre
