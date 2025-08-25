from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Habit, HabitCompletion
from .serializers import HabitSerializer, HabitCompletionSerializer
from datetime import date

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Habit.objects.filter(user=self.request.user)
        return Habit.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], url_path='complete')
    def complete(self, request, pk=None):
        habit = self.get_object()
        today = date.today()
        completion, created = HabitCompletion.objects.get_or_create(habit=habit, date=today)
        if created:
            return Response({'status': 'habit completed for today'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'habit already completed for today'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='uncomplete')
    def uncomplete(self, request, pk=None):
        habit = self.get_object()
        today = date.today()
        deleted_count, _ = HabitCompletion.objects.filter(habit=habit, date=today).delete()
        if deleted_count > 0:
            return Response({'status': 'habit uncompleted for today'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'status': 'habit was not completed today'}, status=status.HTTP_404_NOT_FOUND)
