from django import forms
from .models import StudentGrades

class GradeForm(forms.ModelForm):
    class Meta:
        model = StudentGrades
        fields = '__all__'