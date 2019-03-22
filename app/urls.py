from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/(\w+)',views.index,name='index'),
    url(r'^$',views.index,name='index'),
    url(r'^subclass/',views.subclass,name='subclass'),
    url(r'^index/',views.index,name='index'),
    url(r'^shop/(\w+)',views.shop,name='shop'),
    url(r'^register/',views.register,name='register'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^login/',views.login,name='login'),
    url(r'^checkename/',views.checkename,name='checkename'),
    url(r'^addcart/',views.addcart,name='addcart'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^isselect/',views.isselect,name='isselect'),
    url(r'^dell/',views.dell,name='dell'),
    url(r'^myorder',views.myorder,name='myorder'),
    url(r'^myorder/(\d+)',views.myorder,name='myorders'),
    url(r'^createorder/',views.createorder,name='createorder'),
    url(r'^startpay/(\w+)',views.startpay,name='startpay'),
    url(r'^comment/',views.comment,name='comment'),
    url(r'^getgoods/$', views.getgoods, name='getgoods'),
    url(r'^returnurl/$', views.returnurl, name='returnurl'),  # 支付成功后，客户端的显示
    url(r'^appnotifyurl/$', views.appnotifyurl, name='appnotifyurl'),  # 支付成功后，订单的处理
    url(r'^pay/$', views.pay, name='pay'),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    url(r'^getuserinfo/$', views.getuserinfo, name='getuserinfo'), # 修改信息
    url(r'^upfile/$', views.upfile, name='upfile'), # 头像（文件）上传
    url(r'^upadd/$', views.upadd, name='upadd'), # 更新地址
    url(r'^goodsup/$', views.goodsup, name='goodsup'),# 商品发布
    url(r'^goodsmanage/$', views.goodsmanage, name='goodsmanage'),# 商品发布
    url(r'^goodsdown/$', views.goodsdown, name='goodsdown'),# 商品下架
    url(r'^customerorder/$', views.customerorder, name='customerorder'),
    url(r'^sendgoods/$', views.sendgoods, name='sendgoods'),

]