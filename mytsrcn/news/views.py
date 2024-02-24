from django.shortcuts import render
# from django.http import HttpResponse

from .models import News


# def news_list(request):
#     return HttpResponse('<h1>Новости</h1>')


def news_list(request):
    news = News.objects.all()
    template = 'list.html'
    context = {
        'page_title': 'Новости',
        # 'news': ['n1', 'n2'],
        'news': news,
    }
    return render(request, template, context)
# Create your views here.
