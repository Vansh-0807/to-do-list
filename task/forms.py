from django import forms
from .models import Task, Tag

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 200)
    message = forms.CharField(max_length = 10000, widget=forms.Textarea)
    email = forms.EmailField()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'deadline' : forms.DateTimeInput(attrs = {'type': 'datetime-local'}) 
        } 

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        