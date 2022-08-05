from tkinter import Widget
from turtle import title
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title', 'content', 'categoria', 'imagem', 'status')
