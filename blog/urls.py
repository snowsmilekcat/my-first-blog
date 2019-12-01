from django.urls import path#パス関数のインポート
from . import views#アプリファイル内の全てのビューをインポートする

urlpatterns = [
  path('',views.post_list,name='post_list')#views.pyというビューファイル内のpost_listという名前の関数をルートURLに割り当て
]
