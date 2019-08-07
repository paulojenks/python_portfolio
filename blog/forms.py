from django import forms
from tinymce import TinyMCE

from . import models


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class BlogForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'blog-form-title', 'placeholder': 'Blog Title...'}))
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 5, 'rows': 10}))

    class Meta:
        model = models.Entry
        fields = ['title', 'content']
