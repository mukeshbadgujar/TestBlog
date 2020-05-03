from django.db import models
from django.contrib.auth.models import User # for foreign key
from django.utils.timezone import now # fpr curerent time
# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    auther = models.CharField(max_length=50)
    slug = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.auther


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # cascad = when we delete Post of user in post table so delete this post on this comment also
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True) # self means itself it is foreign key of the table , this is for if we reply of the comment or it is only a comment
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13]  + '... by ' + self.user.username