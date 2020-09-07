from django.http import HttpResponse
#to render templates
from django.shortcuts import render
from .forms import ContactForm
from news.models import Article
# def home_page(request):
#     return HttpResponse("<h1>Hello world</h2>")
def home_page(request):
    qs = Article.objects.all()[:5]
    context = {"title": "Welcome to TST", 'article': qs}
    # if request.user.is_authenticated:
    #     context = {"title": my_title, 'article_post': article_post}
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{ title }}</h1>".format(title=my_title)
    #print(context)
    return render(request,'home.html', context)

def about_page(request):
    return render(request,'about.html',{"title": "About us"})

def contact_page(request):
    #print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us",
        "form": form
    }
    return render(request,'contact_form.html',context)

#1 hour
