from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Hello world</h2>")

def about_page(request):
    return HttpResponse("<h1>about world</h2>")

def contact_page(request):
    return HttpResponse("<h1>contact world</h2>")
#32
