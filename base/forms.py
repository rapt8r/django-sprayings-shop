from django.forms import ModelForm
from .models import Spraying
from django import forms


class SprayingForm(ModelForm):
    class Meta:
        model = Spraying
        fields = '__all__'
