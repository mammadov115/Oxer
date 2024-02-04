from django.db import models
import re
from django.core.exceptions import ValidationError

# Create your models here.


class Contact(models.Model):
    number = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "Contact "
    

class Slider(models.Model):
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Slider"


class About(models.Model):
    bg_image = models.ImageField(upload_to='about_section_images/%Y/%m/%d', null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return "About"


class Classes(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Classes section"


class Image(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='classes_section_images/%Y/%m/%d', null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class BlogsSection(models.Model):
    text = models.TextField()

    def __str__(self):
        return "Blogs Section"
    
    class Meta:
        verbose_name_plural = "Blogs Section"


class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/%Y/%B/%d', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField()
    show_at_home = models.BooleanField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
    def clean(self) :
        if not self.pk and Blog.objects.filter(show_at_home=True).count() >= 2:
                raise ValidationError("Only two blogs can be set to show on the home page.")
                 
        return super().clean()  


class FeedBackSection(models.Model):
    header = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Feedback section"

    class Meta:
        verbose_name_plural = "FeedBackSection"


class FeedBack(models.Model):
    image = models.ImageField(upload_to="feedbacks/photos/%Y/%B/%d", null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural= "Feedbacks"
        verbose_name= "Feedback"

    def __str__(self):
        return self.name
    

class InfoSection(models.Model):
    image = models.ImageField(upload_to="info_section/%Y/%B/%d", null=True, blank=True)
    google_map_embed_link = models.TextField(null=True, blank=True)
    footer_text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural= "Info Section"

    def __str__(self):
        return "Info Section"
    
    def save(self,*args, **kwargs):
        match = re.search(r'<iframe.*?src=["\'](.*?)["\']', self.google_map_embed_link)
        if match:
            self.google_map_embed_link = match.group(1)
        super().save(*args, **kwargs)


class Message(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    number = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField("Sending Date", auto_now_add=True)

    def __str__(self):
        return self.name


class SocialMediaAccount(models.Model):

    class Platforms(models.TextChoices):
        FB = "fb", "Facebook"
        TW = "tw", "Twitter"
        IN = "in", "Linkedin"
        IG = "ig", "Instagram"
        YT = "yt", "Youtube"

    platform = models.CharField(max_length=250, choices=Platforms.choices, null=True, blank=True, unique=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        platform_choice = [choice.label for choice in self.Platforms if choice == self.platform]
        return str(platform_choice[0])