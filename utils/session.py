# -*- coding: utf-8 -*-
# @author: chenhuachao
# @time: 2018/9/13
from blog.models import SessionAuth
import time
import hashlib
import os

class Session(object):
    def setter(self,key,expiretime):
        _token = hashlib.sha1(os.urandom(24)).hexdigest()
        _s = SessionAuth.objects.create(
            user=key,
            token=_token,
            expiretime=expiretime+int(time.time())
        )
        _s.save()
        return _token
    def getter(self,token):
        print(">>>",token)
        token = SessionAuth.objects.filter(token=token).first()
        print(token)
        if not token:
            return False
        else:
            expiretime = token.expiretime
            print(expiretime)
            if time.time()<expiretime:
                return True
            else:
                SessionAuth.objects.filter(token=token).delete()
                return False




session=Session()
