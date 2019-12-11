from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #クラスプロパティ(テーブルの列の元になる)の定義
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):#承認済コメント件数取得
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):#コメントデータ保存用モデル
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')#Postデータに紐づく情報として定義
    #related_name引数によってポストモデルの中からコメントにアクセスできるようにしている。
    author = models.CharField(max_length=200)#文字列型
    text = models.TextField()#テキスト型
    created_date = models.DateTimeField(default=timezone.now)#日付型
    approved_comment = models.BooleanField(default=False)#Bool型

    def approve(self):#承認可否の保存用
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
