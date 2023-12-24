from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Customer

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'password']
