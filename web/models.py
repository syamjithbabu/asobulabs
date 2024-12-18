from django.db import models
from django.utils.text import slugify

# Create your models here.

class Workshop(models.Model):
    workshop_name = models.CharField(max_length=100)
    workshop_desc = models.TextField()
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/')
    image3 = models.ImageField(upload_to='product_images/', default='default_image.jpg')
    slug = models.SlugField(max_length=255, unique=True, null=True)
    
    def __str__(self):
        return self.workshop_name
    
    def save(self, *args, **kwargs):
        value = self.workshop_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    
class SubWorkshop(models.Model):
    sub_workshop_name = models.CharField(max_length=100)
    sub_workshop_content = models.TextField()
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return self.workshop.workshop_name

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_content = models.TextField()
    blog_date = models.DateField()
    blogger_name = models.CharField(max_length=100)
    blog_image = models.ImageField(upload_to='product_images/')
    slug = models.SlugField(max_length=255, unique=True, null=True)

    def __str__(self):
        return self.blog_title
    
    def save(self, *args, **kwargs):
        value = self.blog_title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    linked_in = models.CharField(max_length=500)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    company = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.first_name