import hashlib
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
from app.models import Wheel, Classify, Goods, User, Cart, Order, OrderGoods, Comment


def index(request, fatherid='0'):
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
    index = request.COOKIES.get('index')
    if(fatherid == '0'):
        if index:
            fatherid = "00"+ index +'00'
        else:fatherid = '00000'
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
    coms = goods.comment_set.all()
    data = {
        'goods': goods,
        'user': user,
        'sum':sum,
        'num':num,
        'coms':coms
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

        return render(request, 'order/order.html', context={'order': order})
    return redirect('app:cart')



def myorder(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
        orders = user.order_set.all()
        return render(request, 'order/myorder.html', context={'orders': orders})
    else:
        return redirect('app:login')

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
    # print(request.GET.get('orderid'))

    orderid = request.GET.get('orderid')
    order = Order.objects.get(pk=orderid)

    sum = 0
    for orderGoods in order.ordergoods_set.all():
        sum += float(orderGoods.goods.price[1:]) * orderGoods.num

    # 支付地址信息
    data = alipay.direct_pay(
        subject='iphone8 plus [256G 8G 灰色]',
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
    return redirect('app:index')


def getgoods(request):
    identifier = request.GET.get('identifier')
    order = Order.objects.filter(identifier=identifier).first()
    order.status=3
    order.save()
    datas = {
        'status': 1
    }

    return JsonResponse(datas)