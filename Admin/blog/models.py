from django.db import models
from django.contrib.auth.models import AbstractUser
from slugify import slugify

# Create your models here.
# CustomUser, Post, Comment

# 커스텀 User 모델
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set', # 역참조 이름 지정
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set', # 역참조 이름 지정
    )
    
# 게시글 모델 - Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    # blank=False : admin/form에서 required 옵션을 제거
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    
    # 모델의 save() 함수를 오버라이딩하여, slugify() 적용
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # 한글명의 제목을 slug로 변환합니다.
        # slugify() 함수는 문자열을 URL-friendly한 형식으로 변환합니다.
        super().save(*args, **kwargs)

"""
    related_name 속성
    * 역참조 이름 지정
    - CustomUser 모델에서 posts 속성을 통해 Post 모델에 접근할 수 있게 해줍니다.
    - related_name을 지정하지 않으면, Django는 기본적으로 'post_set'이라는 이름을 사용합니다.
"""

# 댓글 모델 - Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
