from django import forms
from .models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'w3-input','placeholder':'Username'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'w3-input','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
