from django.db import models
from datetime import date


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state_province = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to='author_avatars', null=True, blank=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(help_text='Post content', null=True, blank=True)
    # authors = models.ManyToManyField('Author')
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True, blank=True)
    publication_date = models.DateField()

    def __str__(self):
        return self.title[:15]
    
