from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/(\w+)',views.index,name='index'),
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
    url(r'^myorder/',views.myorder,name='myorder'),
    url(r'^createorder/',views.createorder,name='createorder')

]