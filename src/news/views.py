from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article

def article_detail(request,article_id):
    obj = get_object_or_404(Article, id=article_id)
    # try:
    #     obj = Article.objects.get(id=article_id)
    # except Article.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    template_name = "article_details.html"
    context = {"object": obj}
    return render(request, template_name, context)
