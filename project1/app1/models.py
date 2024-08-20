from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    posted_at = models.DateTimeField()
    posted_by = models.CharField(max_length=500)

    def __str__(self):
        return f"Title: {self.title} \nDescription: {self.description} \nImage: {self.image} \nPosted at: {self.posted_at} \nPosted By: {self.posted_by}"
