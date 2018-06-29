from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField
    user = models.ForeignKey(User, on_delete=models.CASCADE) #글쓴 유저가(주키가) 삭제된경우 같이 다 삭제하라


    def __str__(self):
        return "Board(%s,%s,%d,%s,%d)" % (self.title, self.content, self.hit, str(self.regdate),self.user.id)



