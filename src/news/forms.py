from django import forms

from .models import Article

class ArticlePostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class  ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','slug','content']
