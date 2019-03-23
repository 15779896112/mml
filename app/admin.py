from django.contrib import admin

from .models import User, Classify,Goods,Publish,Cart,Order,Customerorder,OrderGoods,Comment

# 注册

admin.site.register(User)
admin.site.register(Classify)
# admin.site.register(Goods)
admin.site.register(Publish)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Customerorder)
admin.site.register(OrderGoods)
admin.site.register(Comment)
class GoodsAmin(admin.ModelAdmin):
    # 显示字段(需要显示什么字段，就写上什么字段即可)
  list_display = ['name','price','title','num','isdelete']
  # 过滤器(过滤字段)
  list_filter = ['price']
  # 搜索字段
  search_fields = ['pk']
  # 分页(多少条为一页)
  list_per_page = 10





# 注册
admin.site.register(Goods,GoodsAmin)


# class StudentInfo(admin.TabularInline):
#     model = Student
#     extra = 1
#
# class GradeAdmin(admin.ModelAdmin):
#     list_display =  ['pk', 'g_name']
#     inlines = [StudentInfo]
#
# class StudentAdmin(admin.ModelAdmin):
#     list_filter = ['s_grade']
#     list_display =  ['pk', 's_name', 's_score']
#
#
# admin.site.register(Grade, GradeAdmin)
# admin.site.register(Student, StudentAdmin)













