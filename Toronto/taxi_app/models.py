from django.db import models
from django.utils.text import slugify

# Create your models here.
class Ride(models.Model):

    PickupDate=models.DateField()
    PickupTime=models.TimeField()
    PickupLocation=models.CharField(max_length=200)
    DropOff=models.CharField(max_length=200)
    Transfer=models.CharField()
    ExtraTime=models.CharField()




class Post(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=200, unique=True, blank=True)
    content     = models.TextField()
    published   = models.BooleanField(default=False)
    pub_date    = models.DateTimeField(auto_now_add=True)
    featured_img = models.ImageField(upload_to='blog_images/', null=True, blank=True)




    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




