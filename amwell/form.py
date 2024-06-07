from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['is_provider', 'is_patient', 'phone_number']
        widgets = {
            'is_provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter if provider'}),
            'is_patient': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter if patient'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number '}),
            
        }