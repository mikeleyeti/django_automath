from django.db import models


# Create your models here.
class Question(models.Model):
    """
    Modèle de question
    """

    class Theme(models.Model):
        THEME_CHOICES = [
            ('ENT', 'Entiers'),
            ('DEC', 'Démimaux'),
            ('REL', 'Relatifs'),
            ('FON', 'Fonctions'),
            ('LIT', 'Calc. Littéral'),
            ('COM', 'Complexes'),
            ('GEO', 'Géométrie'),
            ('FRA', 'Fractions')
        ]

    class Niveaux(models.Model):
        THEME_NIVEAUX = [
            ('6eme', 'Sixième'),
            ('5eme', 'Cinquième'),
            ('4eme', 'Quatrième'),
            ('3eme', 'Troisième'),
            ('2nde', 'Seconde'),
            ('1ere', 'Première'),
            ('Term', 'Terminale')
        ]

    titre = models.CharField(max_length=200, primary_key=True)
    question = models.TextField(null=True)
    theme = models.CharField(max_length=3, choices=Theme.THEME_CHOICES)
    enonce = models.TextField(null=False)
    niveau = models.CharField(max_length=4, choices=Niveaux.THEME_NIVEAUX)

    def __str__(self):
        return self.titre
