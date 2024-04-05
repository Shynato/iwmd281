from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["auto_increment_id","commande", "status", "date", "description", "serveur", "responsable"]