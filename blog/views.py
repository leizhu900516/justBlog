from django.shortcuts import render_to_response
from blog.models import Broadcast,Article,Message,User
from django.http import JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
import time
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
    method = request.method
    if method == "GET":
        page = request.GET.get("page",1)
        messages = Message.objects.order_by("-addtimes").all()[(page-1)*limit:page*limit]
        return render_to_response('message.html',locals())
    elif method == "POST":
        data = {}
        message = request.POST.get("message")
        return JsonResponse(data)
@csrf_exempt
def broadcast(request):
    '''
    广播修改
    :param request:
    :return:
    '''
    data={}
    if request.method == "POST":
        _broadcast = request.POST.get("broadcast")
        if _broadcast:
            b = Broadcast.objects.create(
                content=_broadcast,
                addtimes=int(time.time())
            )
            b.save()
            data['code'] = 0
            data['msg'] = ""
        else:
            data['code'] = 1
            data['msg'] = "广播内容不能为空"
        return JsonResponse(data)
    else:
        raise Http404
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

def article(request):
    '''
    文章的增、删、改
    :param request:
    :return:
    '''
    data={}
    method=request.method
    if method == "POST":
        #增加
        pass
    if method == "DELETE":
        #删除
        pass
    return JsonResponse(data)