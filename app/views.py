from django.shortcuts import render, redirect
from .models import *
from .forms import MessageForm
# Create your views here.


def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact-section")
 

    slider = Slider.objects.all()
    about = About.objects.first()
    class_section = Classes.objects.first()
    class_images = Image.objects.all()
    blog_section = BlogsSection.objects.first()
    blogs = Blog.objects.filter(show_at_home=True)
    feedback_section = FeedBackSection.objects.first()
    feedbacks = FeedBack.objects.all()
    info_section = InfoSection.objects.first()
    form = MessageForm()
    sm_list = [x for x in SocialMediaAccount.objects.all()]
    social_media_platforms = {x.platform:x.link for x in sm_list}
#    for api development index.html converted to api/index.html
    return render(request, "api/index.html", locals())

def about(request):
    return render(request, "api/about.html")

def classes(request):
    return render(request, "api/class.html")

def blog(request):
    return render(request, "api/blog.html")