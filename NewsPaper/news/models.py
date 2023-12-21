from django.db import models


class Author(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    pass


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    pass
