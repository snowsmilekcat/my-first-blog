from django.shortcuts import render
from django.utils import timezone
from .models import Post#modelsファイル内のPostクラスの参照

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#Postモデルより、データの取り出し。
    return render(request,'blog/post_list.html',{'posts': posts})
