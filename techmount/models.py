from django.db import models

# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    published = models.CharField(max_length=100)
    owner = models.ForeignKey('users.User', related_name='techmount', on_delete=models.CASCADE)

    def __str__(self):
        return self.name