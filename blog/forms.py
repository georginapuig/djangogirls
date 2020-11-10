from django import forms

from .models import Post


class PostForm(forms.ModelForm):

  class Meta:
    model = Post  # we tell Django which model should be used to create this form
    fields = ('title', 'text',)  # which field(s) should end up in our form.
