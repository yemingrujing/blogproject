from rest_framework import viewsets
from blog.models import Post
from .serializers import PostSerializers
from rest_framework.views import APIView
from django.http import JsonResponse
import requests


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = Post.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = PostSerializers


class getMusicInfo(APIView):
    def get(self, request, *args, **kwargs):
        input_name = request.GET.get("input")
        url = 'http://music.wandhi.com/'
        data = {
            'input': input_name,
            'filter': 'name',
            'type': 'qq',
            'page': 1
        }
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '51',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'music.wandhi.com',
            'Origin': 'http://music.wandhi.com',
            'Pragma': 'no-cache',
            'Referer': 'http://music.wandhi.com/?name=%E9%A2%84%E8%B0%8B&type=qq',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        response = requests.post(url, data, headers=headers)
        print(response.json())
        return JsonResponse(response.json(), json_dumps_params={'ensure_ascii': False}, safe=False)

