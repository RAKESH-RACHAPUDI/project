from django  import forms
from application.models import Student

class student_Form(forms.ModelForm):
    class Meta:
        model=Student

        fields='__all__'
