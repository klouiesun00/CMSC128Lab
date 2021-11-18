from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

#User = get_user_model()
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    #full_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]



class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Incorrect username or password")
        return username

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'birthday', 'genres', 'no_of_books']