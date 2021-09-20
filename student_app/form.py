from django import forms
from .models import student


class Student_Form(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
