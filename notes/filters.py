from django_filters.rest_framework import FilterSet
from .models import Note

class NotesFilter(FilterSet):
    class Meta:
        model = Note
        fields = {
            'status':['exact'],
            
        }