from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
    # render()函数中第一个参数是request对象，第二个参数是一个模板名称，
    # 第三个是一个字典类型的可选参数，它将返回一个包含有给定模板根据给定的上下文渲染结果的HttpResponse对象。

def home2(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def home(request):
    return HttpResponse("Hello World, WuJY")

def detail(request, my_agrs):
    post = Article.objects.all()[int(my_agrs)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

'''
def detail(request, my_agrs):
    return HttpResponse("You're looking at my_agrs %s." % my_agrs)
'''

