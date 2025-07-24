from django.db import models

# Create your models here.

class User(models.Model):
    
    @property
    def posts(self):
        return Post.objects.filter(author=self)
    
    @property
    def comments(self):
        return Comment.objects.filter(author=self)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def comments(self):
        return Comment.objects.filter(post=self)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')