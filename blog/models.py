from django.db import models
from django.contrib.auth.models import User  #user 모델과 연결
# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    # Foreign Key란 테이블과 테이블을 연결하기 위해 사용되는 키
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete 유저가 탈퇴하면 연결된글도 같이 삭제
    title = models.CharField(max_length=256)
    #데이터필드
    content = models.TextField()

    # object 형태가 아니라 제목이 보이도록 하는 코드!
    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        db_table ='comment'

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #글 작성자가 사라지면 같이사라짐
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
