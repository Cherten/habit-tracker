from rest_framework import serializers
from .models import Habit, HabitCompletion

class HabitCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitCompletion
        fields = ['id', 'date']

class HabitSerializer(serializers.ModelSerializer):
    completions = HabitCompletionSerializer(many=True, read_only=True)

    class Meta:
        model = Habit
        fields = ['id', 'user', 'name', 'description', 'created_at', 'completions']
        read_only_fields = ['user']
