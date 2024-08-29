from django.db import models
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)

    def __str__(self):
        return f"Title: {self.first_name}"


class Posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    posted_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    # slug = models.SlugField(unique=True, blank=True, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,default=1)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"Title: {self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    text = models.TextField(max_length=100)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Title: {self.text}"
   

class Tag(models.Model):
    caption = models.CharField(max_length=50)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Title: {self.text}"