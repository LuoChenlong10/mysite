from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
#引入定义的模型
from .models import UserProfile,EmailVerifyRecord
#我们看到的这个用户选项是官方通过useradmin这个类注册到后台的，后边继承这个类
from django.contrib.auth.admin import UserAdmin

#取消关联注册
admin.site.unregister(User)

#定义关联对像的样式,stackinline为纵向排列每一行，tabularinline为并排排列
class Userpronfileline(admin.StackedInline):
    model = UserProfile #关联的模型

#关联字段在user内编辑，关联进来
class UserProfileAdmin(UserAdmin):
    inlines = [Userpronfileline]

#注册user模型
admin.site.register(User, UserProfileAdmin)

@admin.register(EmailVerifyRecord)
class Admin(admin.ModelAdmin):
    list_display = ('code',)