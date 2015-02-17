from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=140, help_text="Please enter the title of the post!")
    body = forms.CharField(help_text="Please enter the body of the post!")
    date = forms.DateField(help_text="Please enter the date!")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Post

        fields = ('title', 'body', 'date')
