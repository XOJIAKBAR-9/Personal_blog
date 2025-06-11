from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.conf import settings


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


# Tags of posts mainly involve the posts related to sth for example: Web dev, backend, music or anything
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Experience_at(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    tags = models.ManyToManyField(Tag)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reading_time = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Project(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),  # Not finished projects
        ('In progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In progress')
    created_at = models.DateTimeField()
    repo_link = models.URLField(blank=True, null=True)  # For github could be most probably

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_uni = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.school_uni}"
