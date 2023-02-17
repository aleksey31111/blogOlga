from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Оставьте комментарий здесь',
        'rows': 4,
        'cols': 50
    }))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
