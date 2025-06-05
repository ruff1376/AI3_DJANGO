from post.models import Post
from django.utils import timezone

for i in range(1, 11):
    Post.objects.create(
        title=f"제목 {i}",
        writer="김조은",
        content=f"{i} 번째 내용 입니다.",
        created_at=timezone.now(),
        updated_at=timezone.now(),
    )