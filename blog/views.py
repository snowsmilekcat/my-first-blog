from django.shortcuts import render
from django.utils import timezone
from .models import Post#modelsファイル内のPostクラスの参照
from django.shortcuts import render, get_object_or_404#エラー画面表示のためのインポート

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#Postモデルより、データの取り出し。
    return render(request,'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
