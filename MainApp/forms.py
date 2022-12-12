from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pizza', 'text']
        labels = {'pizza':'Pizza Name','text':''}

        widgets = {'text':forms.Textarea(attrs={'cols':80})}
        
