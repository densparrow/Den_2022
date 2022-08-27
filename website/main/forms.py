from dataclasses import fields
from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task","category"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию: например (важно, срочно, не срочно)'
            }),
                   }
