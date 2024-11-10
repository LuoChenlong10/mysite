#自定义模板标签
from django import template


from blog.models import Category,Sidebar,Post

register = template.Library()#注册模板标签

@register.simple_tag
def get_category_list():
    return Category.objects.all()

@register.simple_tag
def get_sidebar_list():

    return Sidebar.get_sidebar()

@register.simple_tag
def get_new_post():
    # 获取最新文章
    return Post.objects.order_by('-pub_date')[:8]

@register.simple_tag
def get_hot_pv_post():
    # 手动热门推荐
    return Post.objects.order_by('-pv')[:8]

@register.simple_tag
def get_archives():
    # 文章归档
    return Post.objects.dates('add_date', 'month', order='DESC')[:8]