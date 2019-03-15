import hashlib
import random
import time

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django_redis.serializers import json

from app.models import Wheel, Classify, Goods, User


def index(request,fatherid='0'):
    token = request.session.get('token')
    userid = cache.get(token)
    print(userid)
    user = None
    if userid:
        user = User.objects.get(pk=userid)


    wheels = Wheel.objects.all()
    classifys = Classify.objects.all()
    goods_list = Goods.objects.filter(fatherid=fatherid)
    data = {
        'wheels':wheels,
        'classifys':classifys,
        'goods_list':goods_list,
        'user':user,
    }


    return render(request,'index/index.html',context=data)


def subclass(request):
    typeid = request.GET.get('typeid')
    classify = Classify.objects.filter(typeid=typeid).first()
    # 全部分类: 0  # 台式:00000#笔记本:00001
    childtype_list = []
    for item in classify.childtypenames.split('#'):
        item_arr = item.split(':')
        temp_dir = {
            'name': item_arr[0],
            'id': item_arr[1]
        }

        childtype_list.append(temp_dir)
    datas = {
        'childtypenames':classify.childtypenames,
        'childtype_list':childtype_list,

    }


    return JsonResponse(datas)




def shop(request,goodsid):
    token = request.session.get('token')
    userid = cache.get(token)
    print(userid)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
    goods = Goods.objects.get(pk=goodsid)
    data = {
        'goods':goods,
        'user':user
    }
    return render(request,'index/shop.html',context=data)




def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            if user.password == generate_password(password):    # 验证通过

                token = generate_token()
                cache.set(token, user.id, 60*60*24*3)
                request.session['token'] = token
                return redirect('app:index')
            else:   # 密码错误
                return render(request, 'mine/login.html', context={'ps_err': '密码错误'})
        else:   # 不存在
            return render(request, 'mine/login.html', context={'user_err':'用户不存在'})

def logout(request):
    request.session.flush()

    return redirect('app:index')


def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        passoword = generate_password(request.POST.get('password'))
        user = User()
        user.password = passoword
        user.username = username
        user.save()
        token = generate_token()
        cache.set(token, user.id, 60*60*24*3)

        request.session['token'] = token

        return redirect('app:index')


# def checkemail(request):
#     email = request.GET.get('email')
#
#     # 去数据库中查找
#     users = User.objects.filter(email=email)
#     if users.exists():  # 账号被占用
#         response_data = {
#             'status': 0,  # 1可用， 0不可用
#             'msg': '账号被占用!'
#         }
#     else:   # 账号可用
#         response_data = {
#             'status':1,  # 1可用， 0不可用
#             'msg': '账号可用!'
#         }
#
#     # 返回JSON数据
#     return JsonResponse(response_data)
