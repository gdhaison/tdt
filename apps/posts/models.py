from django.db import models
from apps.users.models import User
from django.urls import reverse

class Post(models.Model):
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('posts:list-posts', kwargs={})

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
         
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)
