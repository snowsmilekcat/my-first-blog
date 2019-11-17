from django.contrib import admin
from .models import Post#使用するポストモデルのインポート

admin.site.register(Post)
