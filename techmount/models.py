from django.db import models

# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('users.User', related_name='news', on_delete=models.CASCADE)

    def __str__(self):
        return self.author

class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    news = models.ForeignKey( News, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('users.User', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
