from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'description', 'website', 'email', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aseguramos que no sea obligatorio
        self.fields['image'].required = False
        self.fields['name'].required = True