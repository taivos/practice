from django.forms import CharField, Form, PasswordInput
from django import forms
from django.contrib import auth


class RegistrationForm(Form):
    login = CharField(label='Login', max_length=100, error_messages={'required': 'Enter the login'})
    password = CharField(label='Password', widget=PasswordInput(), error_messages={'required': 'Enter the password'})
    password_again = CharField(label='Repeat password', widget=PasswordInput(), error_messages={'required': 'Enter the password again'})

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            raise forms.ValidationError('Passwords must be the same!')
        return self.cleaned_data


class LoginForm(Form):
    username = forms.CharField(label=u'User name')
    password = forms.CharField(label=u'Password', widget=PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = auth.authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'User name and password are not suitable')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None
