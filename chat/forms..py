from django.forms import ModelForm
from django import forms
from .models import *
import base64

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = Group_msg
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Add message ...', 'class': 'p-4 text-black', 'maxlength' : '1000', 'autofocus': True }),
        }


    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if self.cleaned_data.get('file'):
    #         file = self.cleaned_data['file']
    #         instance.file = base64.b64encode(file.read()).decode('utf-8')
    #     if commit:
    #         instance.save()
    #     return instance
       