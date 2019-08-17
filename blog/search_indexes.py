from haystack import indexes
from .models import Post


# 为 Post 创建一个索引
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # 每个索引里面必须有且只能有一个字段为 document=True，这代表 django haystack 和搜索引擎将使用此字段的内容作为索引进行检索(primary field)。
    # 注意，如果使用一个字段设置了document=True，则一般约定此字段名为text
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
