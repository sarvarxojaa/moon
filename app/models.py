from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog')
    description = models.TextField()

    author = models.CharField(max_length=20)
    is_published = models.BooleanField(default=True)
    create_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()

    is_solved = models.BooleanField(default=False)
    create_ad = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.full_name} :: {self.email}"


class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}::{self.email}"
