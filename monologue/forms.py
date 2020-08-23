from django.forms import ModelForm

from . import models


class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ["name", "email", "content"]
