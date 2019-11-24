from django.urls import path#パス関数のインポート
from . import views#アプリファイル内の全てのビューをインポートする

urlpatterns = [
  path('',views.post_list,name='post_list'),#post_listという名前のビューをルートURLに割り当て
]
