from django.db import models

# Create your models here.

# Création du model qui va contenir les différents taches

class Task(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    commande = models.CharField(max_length = 180)
    status = models.BooleanField(default = False, blank = True)
    date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    description = models.CharField(max_length = 180)
    serveur = models.CharField(max_length = 180)
    responsable = models.CharField(max_length = 180)
    
    def __str__(self):
        return self.auto_increment_id
