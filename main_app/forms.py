from django.forms import ModelForm
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']

        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
