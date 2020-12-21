from django.db import models
from django.utils import timezone
# Create your models here.
class Articles(models.Model):
    STATUS_CHOISES=[
        ('d', 'Draft'),
        ('p', 'published')
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField(max_length= 600)
    image = models.ImageField(upload_to='images')
    published = models.DateField(default=timezone.now)
    status = models.CharField(max_length=1,choices=STATUS_CHOISES)

    def __str__(self):
        return self.title
    