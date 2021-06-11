from django import forms
from django.forms import fields

from .models import Person, Like


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            "photo",
            "email",
            "gender",
            "full_name",
            "longitude",
            "latitude",
        )


class AddLikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ("from_person", "to_person")
