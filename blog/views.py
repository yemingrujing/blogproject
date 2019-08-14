from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown2


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    # 当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post
    # 如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown2.markdown(post.body,
                                   extras=[
                                       'code-friendly', 'fenced-code-blocks', 'footnotes'
                                   ], safe_mode=True)
    return render(request, 'blog/detail.html', context={'post': post})
