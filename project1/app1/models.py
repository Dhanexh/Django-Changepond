from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)


class Posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    posted_at = models.DateTimeField()
    posted_by = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Title: {self.title} \nDescription: {self.description} \nImage: {self.image} \nPosted at: {self.posted_at} \nPosted By: {self.posted_by}"
    
class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    text = models.TextField(max_length=50)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,default=1)