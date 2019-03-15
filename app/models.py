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



class Goods(models.Model):
    fatherid = models.CharField(max_length=10)
    lrp = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    bigimg = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)

    class Meta:
        db_table = 'mml_goods'

class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=255)
    freindword = models.CharField(max_length=30,default='')

    class Meta:
        db_table = 'mml_user'




