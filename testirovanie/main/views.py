from django.shortcuts import render
from django.views.generic import  ListView
from news.models import Articles
def index(request):
    news = Articles.objects.order_by('-time')[0:3]
    return render(request, 'main/index.html', {'news': news})

def about(request):
    return render(request,'main/about.html', {'rer':'ну тут типо про нас написано '})
def contact(request):
    return render(request, 'main/contact.html', {'rer': 'ну тут типо про нас написано '})

