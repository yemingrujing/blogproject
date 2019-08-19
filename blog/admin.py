from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 自定义显示字段
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']
    # 每页显示条目数
    list_per_page = 5
    # 添加快速查询栏
    search_fields = ('title', 'category__name')
    # 创建过滤器
    list_filter = ('create_time', 'category')
    # 降序排列
    ordering = ('-create_time',)
    # list_editable 设置默认可编辑字段
    list_editable = ['category']
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('title', 'author')


# admin.site = myAdminSite(name='management')
admin.site.site_header = '博客后台管理'
admin.site.site_title = '登录'
admin.site.register(Category)
admin.site.register(Tag)
