from easy.database import models


# Create your models here.
class ArticleManager(models.Manager):
    pass


class Article(models.AdminModel):
    """
    一篇文章
    """
    article_id = models.IntegerField(verbose_name='文章编号')
    edit_time = models.DateTimeField(verbose_name='修改时间')  # 第一次创建的时间也是这个
    title = models.CharField(verbose_name='标题', max_length=30)
    author = models.CharField(verbose_name='作者', max_length=30)
    editor = models.CharField(verbose_name='编辑', max_length=30)
    content = models.TextField(verbose_name='内容', max_length=100000)
    creator_id = models.CharField(verbose_name='创建者ID', max_length=10, null=True, blank=True)
    objects = ArticleManager()

    list_display = ("article_id", "edit_time", "title", "author")

    def __str__(self):
        return str(self.title)

    class Meta:
        # 为版本管理，一个文章有多个版本记录，但id相同，按标题获取时应该返回时间最晚的那个
        unique_together = ('article_id', 'edit_time')
        verbose_name = '文章'
        verbose_name_plural = '文章'
