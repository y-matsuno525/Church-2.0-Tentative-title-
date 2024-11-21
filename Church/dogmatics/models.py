from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.utils.timezone import now, timedelta

# プレプリントモデル
class Preprint(models.Model):
    title = models.CharField(max_length=255)  # 論文のタイトル
    abstract = models.TextField(null=True)  
    content = MDTextField()             # 論文内容
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 投稿者
    created_at = models.DateTimeField(auto_now_add=True)  # 投稿日時
    updated_at = models.DateTimeField(auto_now=True)      # 更新日時
    stars = models.ManyToManyField(User, related_name='preprint_stars', blank=True)  # Starをつけたユーザー,preprint.stars.add(user)で増える

    def star_count(self):
        return self.stars.count()  # Star数のカウント

    def __str__(self):
        return self.title

# プレプリント掲示板コメント
class PreprintComment(models.Model):
    preprint = models.ForeignKey(Preprint, on_delete=models.CASCADE, related_name='p_comments')  # 関連プレプリント
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="p_comments_owner", null=True)
    guest_name = models.CharField(max_length=100, null=True) # ユーザー名（ログイン不要なので文字列として保存）
    content = models.TextField()             # コメント内容
    created_at = models.DateTimeField(auto_now_add=True)  # コメント投稿日時

    def __str__(self):
        return f'Comment by {self.user} on {self.preprint.title}'

# 正式な論文モデル
class FormalPaper(models.Model):
    preprint = models.OneToOneField(Preprint, on_delete=models.CASCADE)  # 元のプレプリント
    formalized_at = models.DateTimeField(auto_now_add=True)  # 正式化日時

    def __str__(self):
        return f'Formalized: {self.preprint.title}'

# 正式な論文掲示板コメント
class FormalPaperComment(models.Model):
    paper = models.ForeignKey(FormalPaper, on_delete=models.CASCADE, related_name='f_comments')  # 関連論文
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="f_comments_owner", null=True)
    guest_name = models.CharField(max_length=100, null=True) 
    content = models.TextField()             # コメント内容
    created_at = models.DateTimeField(auto_now_add=True)  # コメント投稿日時

    def __str__(self):
        return f'Comment by {self.user} on {self.paper.preprint.title}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    last_posted_at = models.DateTimeField(null=True, blank=True)  # 最後に投稿した日時

    def can_post(self):
        """投稿可能かチェック"""
        one_week_ago = now() - timedelta(days=7)
        last_post = Preprint.objects.filter(author=self.user).order_by('-created_at').first()#self.user.preprints.order_by('-created_at').first()

        if not last_post:
            return True

        self.last_posted_at = last_post.created_at
        self.save()

        if last_post.created_at >= one_week_ago: #理解後で
            return False
        return True