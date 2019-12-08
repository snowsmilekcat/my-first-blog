from django.urls import path#パス関数のインポート
from . import views#アプリファイル内の全てのビューをインポートする

urlpatterns = [
  path('',views.post_list,name='post_list'),#views.pyというビューファイル内のpost_listという名前の関数をルートURLに割り当て
  path('post/<int:pk>/', views.post_detail, name='post_detail'),#<int:pk>の部分は、int型のpkという変数に対応した値がパスとして続くことを要求するための記載。
]
