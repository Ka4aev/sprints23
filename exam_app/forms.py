from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class Register(UserCreationForm):
    email = forms.EmailField(required=True,label='Почта')
    name = forms.CharField(max_length=150,required=True,label='Имя')
    avatar = forms.ImageField(required=False,label='Аватар')

    class Meta:
        model = User
        fields = ('username','email','name','avatar','password1','password2')



