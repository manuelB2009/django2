from django import forms
from .models import NewsLetter, NewsLetterUser

class NewsLetterUserSignUpForm(forms.ModelForm):
    class meta:
        model=NewsLetterUser
        fields=['email']

class NewsLetterCreationForm(forms.ModelForm):
    class meta:
        model=NewsLetter
        fields=['name', 'subject', 'body', 'email']