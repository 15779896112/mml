import hashlib
import random
import time

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django_redis.serializers import json

from app.models import Wheel, Classify, Goods, User, Cart


def index(request, fatherid='00000'):
    token = request.session.get('token')
    userid = cache.get(token)
    print(userid)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
        sum,num = sumsprice(user)
    else:
        sum= '0'
        num = '0'

    wheels = Wheel.objects.all()
    classifys = Classify.objects.all()
    goods_list = Goods.objects.filter(fatherid=fatherid)
    data = {
        'wheels': wheels,
        'classifys': classifys,
        'goods_list': goods_list,
        'user': user,
        'sum':sum,
        'num':num,
    }

    return render(request, 'index/index.html', context=data)


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
        if item_arr[1] != '0':
            childtype_list.append(temp_dir)
    datas = {
        'childtypenames': classify.childtypenames,
        'childtype_list': childtype_list,

    }

    return JsonResponse(datas)


def shop(request, goodsid):
    token = request.session.get('token')
    userid = cache.get(token)
    print(userid)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
        sum, num = sumsprice(user)
    else:
        sum = '0'
        num = '0'

    goods = Goods.objects.get(pk=goodsid)
    data = {
        'goods': goods,
        'user': user,
        'sum':sum,
        'num':num
    }
    return render(request, 'index/shop.html', context=data)


def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            if user.password == generate_password(password):  # 验证通过

                token = generate_token()
                cache.set(token, user.id, 60 * 60 * 24 * 3)
                request.session['token'] = token
                return redirect('app:index')
            else:
                return render(request, 'mine/login.html', context={'err2': '密码错误'})
        else:
            return render(request, 'mine/login.html', context={'err1': '用户不存在'})


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
        cache.set(token, user.id, 60 * 60 * 24 * 3)

        request.session['token'] = token

        return redirect('app:index')


def checkename(request):
    username = request.GET.get('username')
    users = User.objects.filter(username=username)
    if users.exists():
        response_data = {
            'status': 0,
            'msg': '账号被占用!'
        }
    else:
        response_data = {
            'status': 1,
            'msg': '账号可用!'
        }

    return JsonResponse(response_data)


def cart(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
        carts = Cart.objects.filter(user=user)
        sum,num = sumsprice(user)
        sum_select = selectsprice(user)
        data ={
            'user':user,
            'carts':carts,
            'sum':sum,
            'num':num,
            'sum_select':sum_select
        }
        return render(request, 'cart/cart.html',context=data)
    else:
        return redirect('app:login')


def addcart(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
        goodsid = request.GET.get('goodsid')

        goods = Goods.objects.get(pk=goodsid)
        cart = Cart()
        carts = Cart.objects.filter(goods=goods).filter(user=user)
        if carts.exists():
            cart = carts.first()
            cart.number = int(cart.number) + int(request.GET.get('num'))
            cart.total = float(cart.goods.price[1:])*int(cart.number)
            cart.save()
        else:
            cart.user = user
            cart.goods = goods
            cart.number = request.GET.get('num')
            cart.total = float(goods.price[1:])*int(cart.number)
            cart.save()
        # 统计
        carts = Cart.objects.filter(user=user)
        sum = 0
        num = 0
        for cart in carts:
            sum += float(cart.goods.price[1:])*int(cart.number)
            num += cart.number

        data = {
            'status': 1,
            'msg': '加入购物车成功!',
            'num':num,
            "sum":sum
        }
    else:
        data = {
            'status': 0,
            'msg': '未登录!'
        }
    return JsonResponse(data)


def sumsprice(user):
    carts = Cart.objects.filter(user=user)
    sum = 0
    num = 0
    for cart in carts:
        sum += float(cart.goods.price[1:]) * int(cart.number)
        num += cart.number
    return sum,num



def selectsprice(user):
    sum = 0
    carts = user.cart_set.all()
    for cart in carts:
        if cart.isselect :
            sum += float(cart.goods.price[1:]) * int(cart.number)
    return sum



def isselect(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    cartid = request.GET.get('cartid')
    check = request.GET.get('check')
    carts = user.cart_set.all()
    data = {
        'status':1
    }
    if cartid == 'all' and carts.exists():

        if check == 'yes':
            for cart in carts:
                cart.isselect = True
                cart.save()
        else:
            for cart in carts:
                cart.isselect =False
                cart.save()
    elif carts.exists() and cartid:
        cart = Cart.objects.filter(pk=cartid).first()
        if check=='yes':
            cart.isselect = True
            cart.save()
        else:
            cart.isselect=False
            cart.save()
    else:
        data['status'] = 0


    #求选中的总额
    sum = 0
    for cart in carts:
        if cart.isselect :
            sum += float(cart.goods.price[1:]) * int(cart.number)
    data['sum'] = sum


    return JsonResponse(data)