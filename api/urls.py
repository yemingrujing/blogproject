from django.conf.urls import url, include
from rest_framework import routers
from api import views

# 定义路由地址
route = routers.DefaultRouter()
# 注册新的路由地址
route.register(r'post_list', views.PostViewSet)

# Register your models here.
app_name = 'api'
urlpatterns = [
    url(r'api/', include(route.urls)),
    url(r'api/get/music/info', views.getMusicInfo.as_view()),
    url(r'api/get/blog/detail', views.getBlogDetail.as_view()),
]