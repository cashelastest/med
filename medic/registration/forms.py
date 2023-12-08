from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Post,zapys
class zapysForm(forms.ModelForm):



    name= forms.CharField(max_length = 200)
    problem = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(label='Дата рождения', widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), required=False)

    class Meta:
        model = zapys
        fields = ('name', 'problem', 'date')
class LoginForm(forms.Form):

    username = forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    date = forms.DateField(label='Дата рождения', widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content', 'author', 'time']      