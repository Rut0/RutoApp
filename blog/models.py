from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    tags = models.CharField(max_length=200)
    creationdate = models.DateTimeField()
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
