from django.db import models
import time
# Create your models here.


class Article(models.Model):
    id=models.AutoField(help_text="自增id",primary_key=True)
    content=models.TextField(help_text="文章内容")
    abstract=models.TextField(help_text="摘要")
    title = models.CharField(max_length=255,help_text="标题")
    addtimes = models.IntegerField(help_text="添加时间")
    zan_sum = models.IntegerField(help_text="点赞数",default=0)
    authorid  = models.IntegerField(help_text="作者id")
    coverimg = models.CharField(max_length=255,help_text="封面")
    status = models.SmallIntegerField(help_text="状态",default=0)
    see_num = models.IntegerField(default=0,help_text="浏览量")
    class Meta:
        db_table = "article"
    def get_format_date(self):
        '''
        时间转换函数
        :param addtime:
        :return:
        '''
        localtime = time.time()
        if localtime - self.addtimes < 3600:
            return '{m}分钟前'.format(m=int((localtime - self.addtimes) / 60))
        if 3600 < localtime - self.addtimes < 86400:
            return '{h}小时前'.format(h=int((localtime - self.addtimes) / 3600))
        if 86400 < localtime - self.addtimes < 604800:
            return '{h}天前'.format(h=int((localtime - self.addtimes) / 86400))
        return time.strftime("%Y-%m-%d %H:%M", time.localtime(self.addtimes))

class Broadcast(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(help_text='广播内容')
    addtimes = models.IntegerField(help_text="添加时间")

    class Meta:
        db_table = "broadcast"

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(help_text="留言内容")
    addtimes = models.IntegerField(help_text="添加时间")
    authorid = models.IntegerField(help_text="作者id")
    zan_sum = models.IntegerField(help_text="点赞数",default=0)
    class Meta:
        db_table = "message"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,help_text="姓名")
    addtimes = models.IntegerField(help_text="添加时间")
    sex = models.SmallIntegerField(help_text="性别")
    img = models.CharField(max_length=100,help_text="头像")
    passwd = models.CharField(max_length=100,help_text="密码")
    level = models.SmallIntegerField(help_text="用户级别")
    class Meta:
        db_table = "user"

class SessionAuth(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100,help_text="")
    token = models.CharField(max_length=50,help_text="")
    expiretime = models.IntegerField(help_text="超时时间")
    class Meta:
        db_table = "sessionauth"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    aid = models.IntegerField(help_text="文章id")
    comment = models.TextField(help_text="评论内容")
    addtimes = models.IntegerField()
    uid = models.IntegerField(default=0)
    zan = models.IntegerField(default=0,help_text="点赞数")
    class Meta:
        db_table = "comment"