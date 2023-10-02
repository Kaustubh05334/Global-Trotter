from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from blog.models import BlogPost,AdminComment
from .models import Notification
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
from googletrans import Translator
# Create your views here.


def translate_hindi_to_english(hindi_text):
    translator = Translator()
    translation = translator.translate(hindi_text, src='hi', dest='en')
    english_text = translation.text
    return english_text

@login_required(login_url='/account/login')
def profile_page(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        instagram_link = request.POST.get('instagram_link')
        # profile_image = request.FILES.get('profile_image')
        profile_image = request.FILES.get('profile_image')
        facebook_link = request.POST.get('facebook_link')
        user_bio = request.POST.get('user_bio')
        mobile_number = request.POST.get('mobile_number')

        
        if profile:
            profile.instagram_link = instagram_link
            if profile_image:
                profile.profile_image = profile_image
            profile.facebook_link = facebook_link
            profile.user_bio = user_bio
            profile.mobile_number = mobile_number
            profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('profile_view')

    return render(request, 'userProfile/profile_list.html', {'profile': profile})

def profile_view(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user) 
    except Profile.DoesNotExist:
        profile = Profile.objects.create_profile(user=user, mobile_number='xxxx-xxx-xxx')
    blog_posts = BlogPost.objects.filter(user=user).order_by('-created_at')
    paginator = Paginator(blog_posts, 2)  # Show 5 blog posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    notification = Notification.objects.filter(recipient=user).order_by('-created_at')[:4]
    context={
        'page_obj': page_obj,
        'profile': profile,
        'notifications':notification,

    }
    return render(request, 'userProfile/profile.html', context)

def reject_blog_page(request,ad_id):
    try:
        ac = AdminComment.objects.get(id=ad_id)
        bp = BlogPost.objects.get(id=ac.blog_post.id)
    except AdminComment.DoesNotExist or BlogPost.DoesNotExist:
        url=reverse('catch_all_view')
        return redirect(url)
    context={
        'ac':ac,
        'bp':bp,
    }
    return render(request,'userProfile/reject_blog_page.html',context)

def all_notification(request):
    user = request.user
    notfs = Notification.objects.filter(recipient=user).order_by('-created_at')
    return render(request,'userProfile/allnotf.html',{'notfs':notfs})
