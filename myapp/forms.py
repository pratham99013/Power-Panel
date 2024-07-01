from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Question, Reply

class Tweetform(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title' , 'text', 'photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
  
  class Meta:
    model = User
    fields = ( 'email', 'password')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'photo','text', ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False 

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']

