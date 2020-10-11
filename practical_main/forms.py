from django import forms
from .models import Userprofile


class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = [
            'name',
            'email',
            'country',
            'books_name',
            'isbn',
            'author'
        ]
