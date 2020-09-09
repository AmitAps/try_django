from django import forms

from .models import Article

# class ArticlePostForm(forms.Form):
#     title = forms.CharField()
#     slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)


class  ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','slug','image','content','publish_date']

    def clean_title(self, *args, **kwargs):
        #print(dir(self))
        instance = self.instance
        #print(instance)
        title = self.cleaned_data.get('title')
        qs = Article.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) #id=instance.id
        #print(qs)
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try something else")

        return title
