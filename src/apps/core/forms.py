from django import forms

from .models import Person


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