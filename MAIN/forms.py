from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=255)
	email = forms.EmailField()
	password = forms.CharField(max_length=255, widget=forms.PasswordInput)
	token = forms.CharField(max_length=10)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=255)
	password = forms.CharField(max_length=255, widget=forms.PasswordInput)