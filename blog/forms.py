from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    form to create comments
    """
    class Meta:
        """
        model related to form and fields for edit
        """
        model = Comment
        fields = ('body',)
