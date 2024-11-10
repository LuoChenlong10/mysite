from django.urls import path

from . import views

#定义一个命名空间，用来区分不同应用之间的链接地址
app_name = 'users'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/',views.register,name='register'),
    path('active/<active_code>', views.active_user, name='active_user'),
    #找回密码url
    path('forget_pwd/', views.forget_pwd, name='forget_pwd'),
    path('forget_pwd_url/<active_code>', views.forget_pwd_url, name='forget_pwd_url'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('editor_users/', views.editor_users, name='editor_users'),#编辑用户信息
]