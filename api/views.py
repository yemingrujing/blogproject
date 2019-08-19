from rest_framework import viewsets
from blog.models import Post
from .serializers import PostSerializers


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = Post.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = PostSerializers
