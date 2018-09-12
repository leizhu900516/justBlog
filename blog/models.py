from django.db import models
import time
# Create your models here.


class Article(models.Model):
    id=models.AutoField(help_text="自增id",primary_key=True)
    content=models.TextField(help_text="")
    abstract=models.TextField(help_text="")
    title = models.CharField(max_length=255,help_text="")
    addtimes = models.IntegerField(help_text="")
    zan_sum = models.IntegerField(help_text="",default=0)
    authorid  = models.IntegerField(help_text="")
    coverimg = models.CharField(max_length=255,help_text="封面")
    status = models.SmallIntegerField(help_text="",default=0)
    class Meta:
        db_table = "article"
    def get_format_date(self):
        '''
        时间转换函数
        :param addtime:
        :return:
        '''
        localtime = time.time()
        print(localtime - self.addtimes)
        if localtime - self.addtimes < 3600:
            return '{m}分钟前'.format(m=int((localtime - self.addtimes) / 60))
        if 3600 < localtime - self.addtimes < 86400:
            return '{h}小时前'.format(h=int((localtime - self.addtimes) / 3600))
        if 86400 < localtime - self.addtimes < 604800:
            return '{h}天前'.format(h=int((localtime - self.addtimes) / 86400))
        return time.strftime("%Y-%m-%d %H:%M", time.localtime(self.addtimes))

class Broadcast(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    addtimes = models.IntegerField()

    class Meta:
        db_table = "broadcast"

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(help_text="")
    addtimes = models.IntegerField(help_text="")
    authorid = models.IntegerField(help_text="")
    zan_sum = models.IntegerField(help_text="",default=0)
    class Meta:
        db_table = "message"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,help_text="")
    addtimes = models.IntegerField(help_text="")
    sex = models.SmallIntegerField(help_text="")
    img = models.CharField(max_length=100,help_text="")
    class Meta:
        db_table = "user"