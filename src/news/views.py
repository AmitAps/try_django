from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
from .forms import  ArticleModelForm # ArticlePostForm
from .models import Article

# def article_detail(request,article_id,slug):
#     print("DJANGO SYS:", request.method, request.path, request.user, request.headers,request.headers['User-Agent'])
#     obj = get_object_or_404(Article, id=article_id, slug=slug)
#     # try:
#     #     obj = Article.objects.get(id=article_id)
#     # except Article.DoesNotExist:
#     #     raise Http404
#     # except ValueError:
#     #     raise Http404
#     template_name = "article_details.html"
#     context = {"object": obj}
#     return render(request, template_name, context)


#CRUD

#GET --> Retrive  List

#POST --> Create /update / DELETE

#Create Retrive Update Delete


def article_list_view(request):
    #list out objects
    #could be search
    qs = Article.objects.all() #queryset --> list of python objects
    template_name = "news/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

#forms Form
# def article_create_view(request):
#     #create objects
#     # ? use a form
#     form = ArticlePostForm(request.POST or None)
#     if form.is_valid():
#         #print(form.cleaned_data)
#         obj = Article.objects.create(**form.cleaned_data)
#         form = ArticlePostForm()
#     template_name = "news/form.html"
#     context = {"form": form}
#     return render(request, template_name, context)

#modelform
#@login_required
@staff_member_required
def article_create_view(request):
    #create objects
    # ? use a form
    form = ArticleModelForm(request.POST or None)
    if form.is_valid():
        #print(form.cleaned_data)
        #obj = Article.objects.create(**form.cleaned_data)

        obj = form.save(commit=False)
        obj.user = request.user
        #obj.title = form.cleaned_data.get("title") + "0"
        obj.save()
        #form.save()
        form = ArticleModelForm()
    template_name = "news/form.html"
    context = {"form": form}
    return render(request, template_name, context)


def article_detail_view(request,article_id,slug):
    #1 object --> detail view
    #could be search
    obj = get_object_or_404(Article, id=article_id, slug=slug)
    template_name = "news/details.html"
    context = {"object": obj}
    return render(request, template_name, context)
@staff_member_required
def article_update_view(request,article_id,slug):
    obj = get_object_or_404(Article, id=article_id, slug=slug)
    form = ArticleModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = "news/form.html"
    context = {'title':f'Update {obj.title}', "form": form }
    return render(request, template_name, context)

@staff_member_required
def article_delete_view(request,article_id,slug):
    obj = get_object_or_404(Article, id=article_id, slug=slug)
    template_name = "news/delete.html"
    if request.method == 'POST':
        if request.user == obj.user:
            obj.delete()
        else:
            return HttpResponse('<h1>You do not have permission.</h1>')
        return redirect('/news')
    context = {"object": obj}
    return render(request, template_name, context)
