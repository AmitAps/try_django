from django.http import HttpResponse
#to render templates
from django.shortcuts import render

# def home_page(request):
#     return HttpResponse("<h1>Hello world</h2>")
def home_page(request):
    my_title = "hello there..."
    context = {"title": "my title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1,2,6,4,8]}
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{ title }}</h1>".format(title=my_title)
    #print(context)
    return render(request,'home.html', context)

def about_page(request):
    return render(request,'about.html',{"title": "About us"})

def contact_page(request):
    return render(request,'hello_world.html',{"title": "Contact us"})

#1 hour
