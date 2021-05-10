from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ClientForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class TaskLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]

    def __init__(self, *args, **kwargs):
        super(TaskLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

