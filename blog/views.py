from django.shortcuts import render,render_to_response,redirect
from blog.models import Broadcast,Article,Message,User
# Create your views here.


def manage(request):
    '''
    后台管理
    :param request:
    :return:
    '''
    return render_to_response("manage/manage.html",locals())
def index(request):
    '''
    主页
    :param request:
    :return:
    '''
    articles = []
    limit = 2
    page = int(request.GET.get("page",1))
    broadcost = Broadcast.objects.values("content").order_by("-addtimes").all().first()
    articlelist = Article.objects.order_by("-addtimes").all()[(page-1)*limit:page*limit]

    return render_to_response('index.html',locals())


def messageBoard(request):
    '''
    留言板
    :param request:
    :return:
    '''
    limit = 2
    page = request.GET.get("page",1)
    messages = Message.objects.order_by("-addtimes").all()[(page-1)*limit:page*limit]
    return render_to_response('message.html',locals())

def details(request,articleid):
    '''
    博文详情页
    :param request:
    :return:
    '''
    articleinfo = Article.objects.get(id=articleid)
    return render_to_response('details.html',locals())

def about(request):
    return render_to_response('about.html',locals())

def page_not_found(request):
    return render_to_response('404.html',locals())


def comment(request):
    return render_to_response('comment.html',locals())