"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views
app_name = 'index'
urlpatterns = [
    #  主页
    url(r'^$', views.index, name='index'),

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics')
]