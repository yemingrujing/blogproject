from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import CommentForm


# Create your views here.
def post_comment(request, post_pk):
    # 先获取被评论的文章
    post = get_object_or_404(Post, pk=post_pk)

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            #   # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来。
            comment.post = post

            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            return redirect(post)
        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            comment_list = post.comment_set.all()
            context = {'post': post, 'form': form, 'comment_list': comment_list}
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)
