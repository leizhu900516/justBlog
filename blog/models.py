from django.db import models
import time
# Create your models here.


class Article(models.Model):
    id=models.AutoField(help_text="自增id",primary_key=True)
    content=models.TextField(help_text="")
    title = models.CharField(max_length=255,help_text="")
    addtimes = models.IntegerField(max_length=10,help_text="")
    zan_sum = models.IntegerField(max_length=10,help_text="",default=0)
    authorid  = models.IntegerField(help_text="")
    coverimg = models.CharField(max_length=255,help_text="封面")

    class Meta:
        db_table = "article"
    def get_format_date(self):
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(self.addtimes))

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
    zan_sum = models.IntegerField(help_text="")
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
    '''
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `addtimes` int(11) DEFAULT NULL,
  `sex` tinyint(4) DEFAULT NULL,
  `img` varchar(100) DEFAULT NULL,
    
    '''