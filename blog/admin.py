#admin画面で管理するテーブル情報の管理用ファイル
from django.contrib import admin
from .models import Post,Comment#使用するモデルのインポート

admin.site.register(Post)

admin.site.register(Comment)
