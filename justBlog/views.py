# -*- coding: utf-8 -*-
# @author: chenhuachao
# @time: 2018/9/8
from django.shortcuts import  redirect

def home(request):
    return redirect("/index")