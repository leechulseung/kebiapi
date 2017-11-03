from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contentid = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey('Post' ,related_name='%(app_label)s_%(class)ss')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    related_name='%(app_label)s_%(class)ss')
    msg = models.TextField()
    image = models.ImageField('image', upload_to="media/%y/%d/%m/" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)