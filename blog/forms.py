from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):#投稿用フォーム

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):#コメント用フォーム

    class Meta:
        model = Comment
        fields = ('author', 'text',)
