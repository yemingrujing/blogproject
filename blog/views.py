from django.shortcuts import render, get_object_or_404
from .models import Post, Category
import markdown2
from comments.forms import CommentForm


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
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_first = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post, 'form': form, 'comment_list': comment_first}
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(create_time__day=year, create_time__month=month).order_by('-create_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
