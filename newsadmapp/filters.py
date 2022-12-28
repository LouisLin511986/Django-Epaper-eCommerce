from django import forms
from .models import NewsUnit
import django_filters
 
 
class NewsUnitFilter(django_filters.FilterSet):
 
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
 
    genre = django_filters.CharFilter(
        widget=forms.Select(choices=(('', '請選擇'),) + NewsUnit.GENRE_CHOICES, attrs={'class': 'form-control'}))
 
    Nickname = django_filters.CharFilter(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
 
    class Meta:
        model = NewsUnit
        fields = '__all__'