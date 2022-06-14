from django.db import models
from datetime import datetime
from django . db import models
"""
class Machine(models.Model):
    id = models.AutoField(
                    primary_key = True,
                    editable = False)
    
    nom = models.CharField(
                max_length = 6)

    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom
"""
class Voiture(models.Model):
    id = models.AutoField(
                    primary_key = True,
                    editable = False)
    
    nom = models.CharField(
                max_length = 6)

    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom





# Create your models here .
class Machine ( models.Model ):

    TYPE = (
        ('PC', ('PC - Windows')),
        ('Mac', ('MAc - MacOS')),
        ('Serveur', ('Serveur - Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField ( primary_key =True , editable = False )
    nom = models.CharField ( max_length =6 )
    maintenanceDate = models.DateField ( default = datetime . now ())
    mach = models.CharField ( max_length =32 , choices =TYPE , default ='PC')
    ref = models.CharField ( max_length =10 , default ='0000000000' )
    perso_maint = models.ForeignKey('Personne',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
class Personne ( models.Model ):

    TYPE = (
        ('directeur', ('directeur - en chef')),
        ('sous-directeur', ('sous-directeur - directeur en second')),
        ('ingénieure', ('ingénieure - s occupe de la maintenance des machine')),
        ('technicient', ('technicient - fait des machines')),
    )

    id = models.AutoField ( primary_key =True , editable = False )
    nom = models.CharField ( max_length =6 )
    maintenanceDate = models.DateField ( default = datetime . now ())
    mach = models.CharField ( max_length =32 , choices =TYPE , default ='PC')
    
    def __str__(self):
        return str(self.id) + " -> " + self.nom
    
    