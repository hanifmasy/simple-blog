from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    published_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(('draft', 'Draft'), ('published', 'Published')))

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

class LikesDislikes(models.Model):
    REACTION_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike')
    )
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes_dislikes', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes_dislikes', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

    def __str__(self):
        if self.post:
            return f"{self.user.username} {self.reaction}d {self.post.title}"
        else:
            return f"{self.user.username} {self.reaction}d {self.comment.post.title}'s comment"
