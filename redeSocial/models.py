from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    username = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    website = models.CharField(max_length=300)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Post(models.Model):
    userId = models.ForeignKey(Profile, models.CASCADE, related_name='posts')
    title = models.CharField(max_length=300)
    body = models.TextField()

    class Meta:
        ordering = ('userId',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    postId = models.ForeignKey(Post, models.CASCADE, related_name='comments')
    name = models.CharField(max_length=300)
    email = models.EmailField()
    body = models.TextField()

    class Meta:
        ordering = ('postId',)

    def __str__(self):
        return self.name