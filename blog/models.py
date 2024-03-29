from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Stores a blog post entry related to :model: `auth.user`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        orders posts by date created on
        """
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | By {self.author} | On {self.created_on}"


class Comment(models.Model):
    """
    Stores a comment related to :model:`auth.user`
    and :model:`blog.Post`
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        orders comments by created on
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
