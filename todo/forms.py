from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control border-dark !important",
                }
            ),
            "content": forms.TextInput(
                attrs={
                    "class": "form-control border-dark !important",
                    "placeholder": "What's need to be done ?"
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={"class": "form-control border-dark !important"}
            ),
        }
