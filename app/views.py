from django.shortcuts import render
from .models import *
from .forms import MessageForm
# Create your views here.


def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

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
   
    return render(request, "index.html", locals())