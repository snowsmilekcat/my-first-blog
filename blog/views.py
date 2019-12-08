from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post#modelsファイル内のPostクラスの参照
from django.shortcuts import render, get_object_or_404#エラー画面表示のためのインポート
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#Postモデルより、データの取り出し。
    return render(request,'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":#リクエストがPOSTかどうかで制御を分岐
        form = PostForm(request.POST)
        if form.is_valid():#画面のチェック処理で問題ないかで分岐
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()#更新内容をデータベースに反映
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):#編集のため、今保有しているpkも取得する。
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
