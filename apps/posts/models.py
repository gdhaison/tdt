from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('root', kwargs={})

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse('root', kwargs={})

    class Meta:
        unique_together = [
            ("user", "post"),
        ]
         
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)
