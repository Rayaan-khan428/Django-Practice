from rest_framework import serializers
from .models import Todo

# will convert the model instances to JSON so that the frontend can work with the received data
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

