from django import forms
from .models import task

class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'desc', 'priority', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...',
                'autocomplete': 'off',
            }),
            'desc': forms.Textarea(attrs={
                'class': 'form-control desc-area',
                'placeholder': 'Enter task description (optional)...',
                'rows': 3,
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control',
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
        }
