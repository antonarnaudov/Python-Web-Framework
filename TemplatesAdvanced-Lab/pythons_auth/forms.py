from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from pythons_auth.models import UserProfile

# class RegisterForm(forms.ModelForm): BASIC

'''UserCreationForm CONTAINS out of the box logic such as 2 password inputs and verification'''


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ('username', 'password', 'email')
        # because of UserCreationForm we dont need password field, its already included
        fields = ('username', 'email')

        widgets = {
            # Password field shows dots instead of plain text!
            'password': forms.PasswordInput(),
        }

    '''Extended validation: making email Required!'''

    def clean_email(self):
        # self.cleaned_data['email'] -> No Email = Error
        email = self.cleaned_data.get('email', False)  # If no email, default value is set to False

        if not email:
            raise forms.ValidationError('Email is required.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )
