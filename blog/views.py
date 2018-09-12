from django.shortcuts import render_to_response
from blog.models import Broadcast,Article,Message,User
from django.http import JsonResponse,Http404,QueryDict
from django.views.decorators.csrf import csrf_exempt
import time
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid
import os

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

@csrf_exempt
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
        mess = Message.objects.create(
            content=message,
            addtimes=int(time.time()),
            authorid=1,
        )
        mess.save()
        data['code'] = 0
        data['msg'] = ""
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
@csrf_exempt
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
        params = request.POST
        articleobj=Article.objects.create(
            title=params.get('title'),
            abstract=params.get('abstract'),
            content=params.get("content"),
            addtimes=int(time.time()),
            coverimg=params.get("coverimg"),
            authorid=1,
        )
        articleobj.save()
        data['code'] = 0
        data['msg'] = ""
    if method == "DELETE":
        params = QueryDict(request.body)
        #删除
        Article.objects.get(id=params.get("id")).delete()
        data['code'] = 0
        data['msg'] = ""
    return JsonResponse(data)
@csrf_exempt
def upload(request):
    '''
    图片上传
    :param request:
    :return:
    '''
    data = {}
    images = request.FILES.get("file")
    storage_dir = "/data/media/upload/photo/"
    # imagepath = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    img = '{0}{1}.{2}'.format(storage_dir,uuid.uuid1(), images.name.split('.')[-1])
    try:
        with open(img,'wb') as f:
            f.write(images.read())
        # path = default_storage.save(img, ContentFile(images.read()))
        # tmp_file = os.path.join(imagepath + path)
    except Exception as e:
        data['code'] = 1
        data['msg'] = str(e)
    else:
        data['code'] = 0
        data['msg'] = ''
    data.setdefault('data',{})['src'] = img
    return JsonResponse(data)
def articlelist(request):
    '''
    获取文章列表
    :param request:
    :return:
    '''
    data = {}
    page = int(request.GET.get("page",1))
    limit = int(request.GET.get("limit",10))
    articles = Article.objects.filter(status=0).all()
    pagedata=articles[(page-1)*limit:page*limit]
    for i in pagedata:
        data.setdefault("data",[]).append({
            "id":i.id,
            "title":i.title,
            "addtimes":i.get_format_date()
        })

    data['code'] = 0
    data['message'] = ""
    data['count'] = articles.count()
    return JsonResponse(data)