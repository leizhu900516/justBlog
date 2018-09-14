# -*- coding: utf-8 -*-
# @author: chenhuachao
# @time: 2018/9/13



from Crypto.Cipher import AES
import base64
from django.shortcuts import HttpResponseRedirect
from utils.session import session
#秘钥,此处需要将字符串转为字节
key = b'qwertyuiopzxcvbn'


def pad(text):
    # 加密内容需要长达16位字符，所以进行空格拼接
    while len(text) % 16 != 0:
        text += b' '
    return text

def pad_key(key):
    # 加密秘钥需要长达16位字符，所以进行空格拼接
    while len(key) % 16 != 0:
        key += b' '
    return key
aes = AES.new(pad_key(key), AES.MODE_ECB)



def encrypt(data):
    '''
    AES加密
    :param data:
    :return:
    '''
    encrypted_text = aes.encrypt(pad(data))
    return base64.b64encode(encrypted_text)


def decrypt(data):
    '''
    AES解密
    :param data: 加密后的文本
    :return:
    '''
    return str(aes.decrypt(base64.b64decode(data)),encoding='utf-8',errors="ignore").strip()

def login_auth(func):
    def wrapper(request):
        ticket = request.COOKIES["ticket"]
        status = session.getter(ticket)
        print(status)
        if status:
            return func(request)
        else:
            return HttpResponseRedirect("/login/")
    return wrapper

if __name__ == '__main__':
    text = b'123456'
    aaa=encrypt(text)
    bbb=decrypt(aaa)
    print(aaa)
    print(bbb)