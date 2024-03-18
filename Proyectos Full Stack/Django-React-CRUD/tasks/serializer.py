from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        #fields = ('id','title','description','done') # Añadir los campos en formato en JSON
        model = Task
        fields = '__all__'
        