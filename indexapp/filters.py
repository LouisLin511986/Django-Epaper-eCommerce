from django import forms
from .models import *
import django_filters
 

class ProductModelFilter(django_filters.FilterSet):

    pname = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入書名'}))
 
    pprice = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入價格'})) 
    pdescription = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入內文關鍵字'}))
    class Meta:
        model = ProductModel
        exclude = ['pimages', 'uploadedFile']
        fields = '__all__'