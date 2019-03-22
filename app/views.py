import hashlib
import os
import random
import time

from urllib.parse import parse_qs
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django_redis.serializers import json

from app.alipay import alipay
from app.models import Wheel, Classify, Goods, User, Cart, Order, OrderGoods, Comment, Publish, Customerorder
from mml import settings


def index(request, fatherid='0'):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
        sum,num = sumsprice(user)
        carts = Cart.objects.filter(user=user)
        carts = carts.order_by('-id')
        orders = user.order_set.all()
        orders = orders.order_by('-id')
        num1,num2,num3 = getordernum(user)
    else:
        sum= '0'
        num = '0'
        orders = ''
        carts = ''
        num1 = '0'
        num2 = '0'
        num3 = '0'


    wheels = Wheel.objects.all()
    classifys = Classify.objects.all()
    index = request.COOKIES.get('index')
    if(fatherid == '0'):
        if index:
            fatherid = "00"+ index +'00'
        else:fatherid = '00000'
    goods_list = Goods.objects.filter(fatherid=fatherid).filter(isdelete=False)

    data = {
        'wheels': wheels,
        'classifys': classifys,
        'goods_list': goods_list,
        'user': user,
        #购物车数量价钱
        'sum':sum,
        'num':num,
        'carts':carts,
        'orders':orders,
        # 订单数量（默认0）
        'num1':num1,
        'num2':num2,
        'num3':num3,

    }

    return render(request, 'index/index.html', context=data)

def getordernum(user):
    num1 = Order.objects.filter(user=user).filter(status='0').count()

    num2 = Order.objects.filter(user=user).filter(status='2').count()
    num3 = Order.objects.filter(user=user).filter(status='3').count()
    # print(num1,num2,num3)
    return num1,num2,num3

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

    user = None
    if userid:
        user = User.objects.get(pk=userid)
        sum, num = sumsprice(user)
        carts = Cart.objects.filter(user=user)
        carts = carts.order_by('-id')
        orders = user.order_set.all()
        orders = orders.order_by('-id')
        num1, num2, num3 = getordernum(user)


    else:
        sum = '0'
        num = '0'
        carts = ''
        orders = ''
        num1=0
        num2=0
        num3=0

    goods = Goods.objects.get(pk=goodsid)
    coms = goods.comment_set.all()
    coms = coms.order_by('-id')
    data = {
        'goods': goods,
        'user': user,
        'sum':sum,
        'num':num,
        'coms':coms,
        'carts':carts,
        'orders':orders,
        'num1': num1,
        'num2': num2,
        'num3': num3
    }
    return render(request, 'index/shop.html', context=data)


def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        tel = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(tel=tel)
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
        tel = request.POST.get('tel')
        user = User()
        user.password = passoword
        user.username = username
        user.tel = tel
        user.save()
        token = generate_token()
        cache.set(token, user.id, 60 * 60 * 24 * 3)

        request.session['token'] = token

        return redirect('app:index')


def checkename(request):
    tel = request.GET.get('tel')
    users = User.objects.filter(tel=tel)
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
        carts =carts.order_by('-id')
        num1, num2, num3 = getordernum(user)
        sum,num = sumsprice(user)
        sum_select = selectsprice(user)
        data ={
            'user':user,
            'carts':carts,
            'sum':sum,
            'num':num,
            'sum_select':sum_select,
            'num1':num1,
            'num2': num2,
            'num3': num3
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
        cart = Cart.objects.filter(id=cartid).first()
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


def dell(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    cartid = request.GET.get('cartid')
    cart = Cart.objects.filter(pk=cartid)
    cart.delete()
    sum = selectsprice(user)
    data = {
        'status': 1,
        'sum':sum
    }
    return JsonResponse(data)



def create_identifier():
    identifier = str(int(time.time()))+str((random.randrange(1000,10000)))
    return identifier

def createorder(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.filter(isselect='True')
    if carts.exists():
        order = Order()
        order.user = user
        order.identifier = create_identifier()


        order.save()

        for cart in carts:
            ordergoods = OrderGoods()
            ordergoods.order = order
            ordergoods.goods = cart.goods
            ordergoods.num = cart.number
            ordergoods.total = float(cart.goods.price[1:]) * int(cart.number)
            ordergoods.save()
            cart.delete()

            # 商家订单
            customerorder = Customerorder()
            customerorder.user = cart.goods.publish.user
            customerorder.order =order
            customerorder.save()


        return render(request, 'order/order.html', context={'order': order})
    return redirect('app:cart')



def myorder(request,s='6'):
    token = request.session.get('token')
    userid = cache.get(token)
    print('status',s)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
        if s == '6':
            orders = user.order_set.all()
        else:
            orders = Order.objects.filter(user=user).filter(status=s)
        orders = orders.order_by('-id')
        return render(request, 'order/myorder.html', context={'orders': orders})
    else:
        return redirect('app:login')


def startpay(request,orderid):
    order = Order.objects.get(pk=orderid)
    return render(request, 'order/order.html', context={'order': order})


def goodsdetail(request,identifier):
    order = Order.objects.filter(identifier=identifier).first()

    return render(request, 'order/order.html', context={'order': order})




def comment(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    goodsid = request.POST.get('goodsid')
    comment = request.POST.get('comment')
    identifier = request.POST.get('identifier')
    goods = Goods.objects.get(pk=goodsid)
    comm = Comment()
    comm.user = user
    comm.goods = goods
    comm.comment = comment
    comm.save()
    print(identifier)
    order = Order.objects.filter(identifier=identifier).first()
    order.status=4
    order.save()

    return redirect('app:myorder')






@csrf_exempt
def appnotifyurl(request):
    if request.method == 'POST':
        # 获取到参数
        body_str = request.body.decode('utf-8')

        # 通过parse_qs函数
        post_data = parse_qs(body_str)

        # 转换为字典
        post_dic = {}
        for k,v in post_data.items():
            post_dic[k] = v[0]

        # 获取订单号
        out_trade_no = post_dic['out_trade_no']

        # 更新状态
        Order.objects.filter(identifier=out_trade_no).update(status=1)


    return JsonResponse({'msg':'success'})


def pay(request):
    # print(request.GET.get('orderid'))update(status=1)

    orderid = request.GET.get('orderid')
    order = Order.objects.get(pk=orderid)
    stri = ''
    sum = 0
    for orderGoods in order.ordergoods_set.all():
        sum += float(orderGoods.goods.price[1:]) * orderGoods.num
        stri += orderGoods.goods.name + '  '

    # 支付地址信息
    data = alipay.direct_pay(
        subject=stri,
        out_trade_no=order.identifier,    # 订单号
        total_amount=str(sum),   # 支付金额
        return_url='http://47.101.216.171/returnurl/'

    )

    # 支付地址
    alipay_url = 'https://openapi.alipaydev.com/gateway.do?{data}'.format(data=data)

    response_data = {
        'msg': '调用支付接口',
        'alipayurl': alipay_url,
        'status': 1
    }
    return JsonResponse(response_data)


def returnurl(request):
    return redirect('app:myorder')


def getgoods(request):
    identifier = request.GET.get('identifier')
    order = Order.objects.filter(identifier=identifier).first()
    order.status=3
    order.save()
    datas = {
        'status': 1
    }

    return JsonResponse(datas)


def userinfo(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)

        if request.method == 'GET':
            return render(request, 'mine/userinfo.html',context={'user':user})
        elif request.method == 'POST':
            username = request.POST.get('username')
            passoword = request.POST.get('password')

            sex = request.POST.get('sex')
            old = request.POST.get('old')
            if passoword:
                user.password=passoword = generate_password(passoword)
            user.sex = sex
            user.username = username
            user.old = old
            user.save()

            return redirect('app:index')
    else:
        return redirect('app:login')


def getuserinfo(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    data = {
        'name':user.username,
        'sex':user.sex,
        'old':user.old,
        'add':user.add,
    }
    return  JsonResponse(data)


def upfile(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)

        if request.method == 'GET':
            return render(request, 'mine/upfile.html')
        elif request.method == 'POST':

            file = request.FILES['file']


            file.name = str(time.time())
            filepath = os.path.join(settings.MDEIA_ROOT, file.name)
            with open(filepath, 'wb') as fp:
                for info in file.chunks():
                    fp.write(info)
            user.img = file.name
            user.save()

            return redirect('app:index')
    else:
        return redirect('app:login')


def upadd(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)

        if request.method == 'GET':
            return render(request, 'mine/upadd.html',context={'user':user})
        elif request.method == 'POST':

            addr = request.POST.get('addr')

            if addr:

                user.add = addr
                user.save()

            return redirect('app:index')
    else:
        return redirect('app:login')



def goodsup(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)

        if request.method == 'GET':
            return render(request, 'mine/goodsup.html')
        elif request.method == 'POST':
            goods = Goods()
            goodsname = request.POST.get('goodsname')
            price = request.POST.get('price')
            title = request.POST.get('title')
            num = request.POST.get('num')
            type = request.POST.get('type')
            file = request.FILES['file']
            file.name = str(time.time()) + str(file.name)
            filepath = os.path.join(settings.GOODSIMG_ROOT, file.name)
            with open(filepath, 'wb') as fp:
                for info in file.chunks():
                    fp.write(info)
            goods.img = 'img/' + file.name
            goods.bigimg = 'img/' + file.name
            goods.name = goodsname
            goods.price = "￥"+price
            goods.num = num
            goods.title = title
            goods.fatherid = type
            goods.save()
            publish = Publish()
            publish.goods = goods
            publish.user = user
            publish.save()
            return redirect('app:index')
    else:
        return redirect('app:login')


def goodsmanage(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        publishs = user.publish_set.all()
        data = {
            'publishs':publishs
        }
        return render(request,'mine/goodsmanage.html',context=data)
    else:
        return redirect('app:login')

# 商品下架
def goodsdown(request):

    goodsid = request.GET.get('goodsid')
    print(goodsid)
    goods = Goods.objects.get(pk=goodsid)
    publish = goods.publish
    publish.isdelete = not publish.isdelete
    goods.isdelete = not goods.isdelete
    publish.save()
    goods.save()
    data = {
        'states':'1'
    }
    return JsonResponse(data)

# 顾客订单
def customerorder(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        publishes = user.customerorder_set.all()
        return render(request, 'mine/customerorder.html', context={'publishes': publishes})
    else:
        return redirect('app:login')


def sendgoods(request):
    identifier = request.GET.get('identifier')
    order = Order.objects.filter(identifier=identifier).first()
    # print(identifier)
    order.status = 2
    order.save()
    datas = {
        'status': 1
    }

    return JsonResponse(datas)