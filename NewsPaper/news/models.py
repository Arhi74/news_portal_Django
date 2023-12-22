from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(author=self).aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        comment_rating = Comment.objects.filter(user=self.user).aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        post_comment_rating = Comment.objects.filter(post__author=self).aggregate(pcr=Coalesce(Sum('rating'), 0))['pcr']

        self.rating = post_rating * 3 + comment_rating + post_comment_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    article = 'Article'
    news = 'News'

    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, choices=POSITIONS, default=news)
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=255)
    text = models.TextField(default='')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

