from django.shortcuts import render
from .models import *
from .forms import MessageForm
# Create your views here.


def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    contact_info = Contact.objects.first()
    slider = Slider.objects.all()
    about = About.objects.first()
    class_section = Classes.objects.first()
    class_images = Image.objects.all()
    blog_section = BlogsSection.objects.first()
    blogs = Blog.objects.all()
    feedback_section = FeedBackSection.objects.first()
    feedbacks = FeedBack.objects.all()
    info_section = InfoSection.objects.first()
    form = MessageForm()
    sm_list = [x for x in SocialMediaAccount]
    social_media_platforms = {key:value for key,value in sm_list.items()}
   
    return render(request, "index.html", locals())