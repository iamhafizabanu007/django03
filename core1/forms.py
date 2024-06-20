from .models import Students
from django import forms

class AddStudentForm(forms.ModelForm):     
        class Meta:
            model = Students
            fields = ("name","roll","city")
    