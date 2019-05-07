from django import forms
from .models import UserText


class UserTextForm(forms.ModelForm):
	class Meta:
		model = UserText
		fields = '__all__'
		widgets = {
            'user': forms.HiddenInput(),
            'uuid': forms.HiddenInput(),
            'text': forms.Textarea(attrs={'placeholder': 'Max. 10000 characters.'})
        }