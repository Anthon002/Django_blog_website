import django_filters
from .models import *

class SearchFilter(django_filters.FilterSet):
    class Meta:
        model= Post
        fields = '__all__'
        exclude = ['liked','profile','content']