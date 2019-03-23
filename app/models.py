from django.db import models

# Create your models here.
class Wheel(models.Model):
    bg = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'mml_wheel'

# typeid,typename,childtypenames
# values("000","电脑","全部分类:0#台式:00000#笔记本:00001"),
# ("001","手机","全部分类:0#苹果:00100#其他:00101"),
# ("002","生活","全部分类:0#母婴:00200#零食:00201#办公:00202#生活用品:00203"),

# 产品分类
class Classify(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=100)

    class Meta:
        db_table = 'mml_types'
    def __str__(self):
        return self.typename



class Goods(models.Model):
    name = models.CharField(max_length=20,default='弄啥嘞')
    fatherid = models.CharField(max_length=10)
    lrp = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    bigimg = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    num = models.CharField(max_length=100,default='1')
    isdelete = models.BooleanField(default=False)  # 是否下架

    class Meta:
        db_table = 'mml_goods'
    def __str__(self):
        return self.name




class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    tel = models.CharField(max_length=30,unique=True)
    img = models.CharField(max_length=50,default='wzh.jpg')
    add = models.CharField(max_length=200,default='')
    sex = models.CharField(max_length=10,default='')
    old = models.CharField(max_length=10,default='')
    class Meta:
        db_table = 'mml_user'

    def __str__(self):
        return self.username

class Publish(models.Model):    # 用户发布商品
    goods = models.OneToOneField(Goods)
    user = models.ForeignKey(User)
    isdelete = models.BooleanField(default=False)  # 是否下架
    createtime = models.DateTimeField(auto_now_add=True) # 创建时间
    updatetime = models.DateTimeField(auto_now=True)
    # states = 0   # 状态


    def __str__(self):
        return self.createtime


class Cart(models.Model):

    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    number = models.IntegerField()
    isselect = models.BooleanField(default=True)
    isdelete = models.BooleanField(default=False)
    total = models.FloatField(default=0)

    class Meta:
        db_table = 'mml_cart'

    def __str__(self):
        return self.user


class Order(models.Model):
    user = models.ForeignKey(User)
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    # -1 过期
    # 0 未付款
    # 1 已付款，待发货
    # 2 已发货，待收货
    # 3 已收货，待评价
    # 4 已评价
    status = models.IntegerField(default=0)
    identifier = models.CharField(max_length=256)

    def __str__(self):
        return self.identifier

class Customerorder(models.Model):
    user = models.ForeignKey(User)
    order = models.OneToOneField(Order)

    def __str__(self):
        return self.order



class OrderGoods(models.Model):
    order = models.ForeignKey(Order)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField()
    total = models.FloatField(default=0)



class Comment(models.Model):
    createtime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.createtime


