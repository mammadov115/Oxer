from django.db import models

# Create your models here.

class Contact(models.Model):
    number = models.CharField(max_length=25)
    email = models.EmailField()
    location = models.CharField(max_length=500)
    g_map = models.TextField(verbose_name='Google map embed link')

    def __str__(self):
        return "Contact "

class Slider(models.Model):
    text = models.TextField()

    def __str__(self):
        return "Slider"

class About(models.Model):
    bg_image = models.ImageField(upload_to='about_section_images/%Y/%m/%d')
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return "About"
    
class Classes(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return "Classes section"
    
class Image(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='classes_section_images/%Y/%m/%d')
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/%Y/%B/%d')
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField()
    text = models.TextField()

    def __str__(self):
        return self.title
    
    