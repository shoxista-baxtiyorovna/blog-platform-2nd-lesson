from django.db import models
from django.utils.text import slugify
from authors.models import Author
from categories.models import Category


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES=(
        ('ac', 'Active'),
        ('pd', 'Pending'),
        ('in', 'Inactive'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

