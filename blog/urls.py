"""justBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog import views


urlpatterns = [
    path('manage/', views.manage),#后台管理
    path('login/', views.login),#登录管理
    path('index/', views.index), #主页
    path('about/', views.about), #关于
    path('article/', views.article), #文章api-restful
    path('upload/', views.upload), #上传api
    path('article/list/', views.articlelist), #文章列表api
    path('message/', views.messageBoard),#留言api
    path('broadcast/', views.broadcast), #公告api
    path('comment/', views.comment), #评论api
    path('article/<int:articleid>.html', views.details),#文章详情页
    path('test/', views.test),
]
