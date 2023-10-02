from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .forms import BlogPostForm,CommentForm,AdminCommentForm,ReportForm
from .models import BlogPost,SubBlogPost,AdminComment,Comment,Report
from django.urls import reverse,reverse_lazy
from userProfile.models import Notification
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from django.utils.text import slugify
from googletrans import Translator
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
from django.contrib.sessions.models import Session
import re

def format_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'//(.*?)//', r'<i>\1</i>', text)
    return text
# Create your views here.

def convert_to_webp(file):
    # Open the image file
    image = Image.open(file)
    output_buffer = io.BytesIO()
    image.save(output_buffer, format='WebP')
    output_buffer.seek(0)

    return output_buffer


def translate_hindi_to_english(hindi_text):
    translator = Translator()
    translation = translator.translate(hindi_text, src='hi', dest='en')
    english_text = translation.text
    return english_text

@login_required(login_url='/account/login')
def like_blog(request,title,blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        url = reverse('catch_all_view')
        return redirect(url)
    
    slug = slugify(translate_hindi_to_english(blog.title))
    
    if title != slug:
        url = reverse('blog_details', kwargs={'title': slug, 'blog_id': blog_id})
        return redirect(url)
    is_liked = blog.likes.filter(id=request.user.id).exists()
    if is_liked:
        blog.likes.remove(request.user)
    else:
        notf = Notification(recipient=blog.user,message=f'{request.user} liked your blog {blog.title}',link=reverse('blog_details', kwargs={'title':slug, 'blog_id':blog_id}))
        notf.save()
        blog.likes.add(request.user)
    blog.save()
    return HttpResponseRedirect(reverse('blog_details', kwargs={'title': slug, 'blog_id': blog_id}))


@login_required
def blogPostPage(request):
    if request.method == 'POST':
            #form = BlogPostForm(request.POST, request.FILES)
            title = request.POST.get('title')
            location = request.POST.get('location')
            content = request.POST.get('content')
            thumbnail =request.FILES.get('thumbnail')
            category = request.POST.get('category')
            #change
            webp_buffer = convert_to_webp(thumbnail)
            webp_image = InMemoryUploadedFile(
                webp_buffer,
                None,
                thumbnail.name + '.webp',
                'image/webp',
                webp_buffer.tell,
                None
            )
            # Access the subform data
            arrSH,arrSL,arrSI,arrST=[],[],[],[]
            for i in range(10):
                subheading = request.POST.get(f'subheading{i+1}')
                subloc = request.POST.get(f'subloc{i+1}')
                subimage =request.FILES.get(f'subimage{i+1}')
                subtext = request.POST.get(f'subtext{i+1}')
                if subheading or subloc or subimage or subtext:
                    arrSH.append(subheading) 
                    arrSL.append(subloc) 
                    arrSI.append(subimage) 
                    arrST.append(subtext)
            user = request.user
            b1 = BlogPost(user=user,thumbnail=webp_image,location=location,title=title,content=content,category=category)
            b1.save()
            slug = slugify(translate_hindi_to_english(b1.title))
            for i in range(len(arrSH)):
                webp_buffer = convert_to_webp(arrSI[i])
                webp_image = InMemoryUploadedFile(
                    webp_buffer,
                    None,
                    arrSI[i].name + '.webp',
                    'image/webp',
                    webp_buffer.tell,
                    None
                )
                sb=SubBlogPost(subheading=arrSH[i],location=arrSL[i],image=webp_image,text=arrST[i])
                sb.save()
                b1.sub_posts.add(sb)
            url = reverse('preview_blog', kwargs={'title':slug,'blog_id': b1.id})
            return redirect(url)
     
    else:
        return render(request,'blog/blogPost.html',{'form':BlogPostForm})

def preview_blog(request,title, blog_id):
    try :
        blog = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        url = reverse('catch_all_view')
        return redirect(url)
    slug = slugify(translate_hindi_to_english(blog.title))
    if request.user == BlogPost.objects.get(id=blog_id).user:
        blog = BlogPost.objects.get(id=blog_id)
        sub_posts = blog.sub_posts.all()
    else:
        url = reverse('catch_all_view')
        return redirect(url)

    if request.method == 'POST' and blog.status == 0:
        title = request.POST.get('title')
        location = request.POST.get('location')
        content = request.POST.get('content')
        thumbnail = request.FILES.get('thumbnail')
        
        blog.title = title
        blog.location = location
        blog.content = format_text(content)

        if thumbnail:
            blog.thumbnail.save(thumbnail.name, thumbnail)

        blog.save()

        for sub_post in sub_posts:
            subheading = request.POST.get(f'subheading{sub_post.id}')
            subloc = request.POST.get(f'location{sub_post.id}')
            image = request.FILES.get(f'image{sub_post.id}')
            text = request.POST.get(f'text{sub_post.id}')

            sub_post.subheading = format_text(subheading)
            sub_post.location = subloc

            if image:
                webp_buffer = convert_to_webp(image)
                webp_image = InMemoryUploadedFile(
                    webp_buffer,
                    None,
                    image.name + '.webp',
                    'imagess/webp',
                    webp_buffer.tell,
                    None
                )
                sub_post.image = webp_image

            sub_post.text = text
            sub_post.save()

        return redirect('profile_view')
    elif blog.status == 1:
        return redirect('blog_details', title=slug, blog_id=blog_id)

    return render(request, 'blog/blogPreview.html', {'blog': blog, 'sub_posts': sub_posts})


def blog_details(request,title, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        url = reverse('catch_all_view')
        return redirect(url)
    slug = slugify(translate_hindi_to_english(blog.title))
    if title != slug:
        url = reverse('blog_details', kwargs={'title': slug, 'blog_id': blog_id})
        return redirect(url)
    is_liked = blog.likes.filter(id=request.user.id).exists()
    like_count = blog.total_likes()
    
    session_key = f"blog_view_{blog_id}"
    if not request.session.get(session_key, False):
        blog.views_count += 1
        blog.save()
        request.session[session_key] = True

    if request.method == 'POST':
        form1 = AdminCommentForm(request.POST)
        form2 = CommentForm(request.POST)

        if form1.is_valid():
            status = form1.cleaned_data['status']
            content = form1.cleaned_data['content']

            if status == 'Approve':
                blog.status = 1
                blog.save()
                notf = Notification(recipient=blog.user,message=f'The blog titled {blog.title} approved',link = reverse_lazy('blog_details', kwargs={'title':slug, 'blog_id': blog.id}))
                notf.save()
                return redirect('approve_page')
            else:
                ac = AdminComment(comment=content, blog=blog)
                ac.save()
                notf = Notification(recipient=blog.user,message=f'The blog titled {blog.title} rejected',link=reverse_lazy('rejected_notf',kwargs={'ad_id':ac.id}))
                notf.save()
                return redirect('approve_page')
        elif form2.is_valid():
            comment_id = request.POST.get('comment_id')
            reply_id = request.POST.get('reply_id')
            reply_to = Comment.objects.get(id=comment_id) if comment_id else None
            user=request.user

            if reply_id != "None" and reply_id is not None:
                reply_at_id=Comment.objects.get(id=reply_id)
                new_comment = Comment(user=user, text=f"@{reply_at_id.user.username} {form2.cleaned_data['content']}")
                new_comment.save()
                
                reply_at_comment = Comment.objects.get(id=comment_id)
                reply_at_comment.replies.add(new_comment)
                reply_at_comment.save()
                url = reverse_lazy('blog_details', kwargs={'title':slug, 'blog_id': blog_id})+f'#reply{new_comment.id}'
                notf = Notification(recipient=reply_at_id.user,message=f'{request.user} tagged you',link=url)
                notf.save()
                return redirect(url)
            else:
                new_comment = Comment(user=user, text=form2.cleaned_data['content'])
                new_comment.save()
                if reply_to:
                    reply_to.replies.add(new_comment)
                    reply_to.save()
                    url = reverse_lazy('blog_details', kwargs={'title':slug,'blog_id': blog_id})+f'#reply{new_comment.id}'
                    if reply_to is not None:
                        notf = Notification(recipient=reply_to.user,message=f'{request.user} replied on your comment',link=url)
                        notf.save()
                else:
                    blog.comments.add(new_comment)
                    blog.save()
                    url = reverse_lazy('blog_details', kwargs={'title':slug, 'blog_id': blog_id})+f'#comment{new_comment.id}'
                    if reply_to is not None:
                        notf = Notification(recipient=blog.user,message=f'{request.user} commented on your blog',link=url)
                        notf.save()                   
            return redirect(url)
    else:
            form = AdminCommentForm() if blog.status == 0 else CommentForm()
    comments = blog.comments.all()
    context={
        'blog': blog,
        'form': form,
        'comments': comments,
        'ac': AdminComment.objects.filter(blog=blog),
        'is_liked':is_liked,
        'like_count':like_count,
        'views_count': blog.views_count,
    }
    return render(request, 'blog/blogDetail.html', context)

@login_required
def delete_blog(request, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        url = reverse('catch_all_view')
        return redirect(url)
    comments = blog.comments.all()
    subps = blog.sub_posts.all()
    if request.method == 'POST' and request.user == blog.user:
        for comment in comments:
            comment.delete()
        for subp in subps:
            subp.delete()
        blog.delete()
        return redirect(reverse('profile_view'))
    return render(request, 'blog/confirmDelete.html', {'blog': blog})

@login_required
def delete_comment(request, blog_id, comment_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    comment = get_object_or_404(Comment, id=comment_id)
    replies = comment.replies.all()

    if request.method == 'POST':
        for reply in replies:
            reply.delete()
        comment.delete()
        return redirect('blog_details', blog_id=blog_id)
    return render(request, 'blog/confirmDelete.html', {'blog': blog, 'comment': comment})

def search(request):
    query = request.GET.get('search')
    if query:
        blog_posts = BlogPost.objects.all().order_by( '-id')

        # Perform fuzzy search using fuzzysearch library
        blogs = []
        for post in blog_posts:
            title_similarity = fuzz.token_sort_ratio(query, post.title)
            location_similarity = fuzz.token_sort_ratio(query, post.location)
            # Adjust the similarity threshold as per your preference
            if title_similarity > 50 or location_similarity > 70:
            # title_matches = find_near_matches(query, post.title, max_l_dist=3)  # Adjust max_l_dist as per your preference
            # location_matches = find_near_matches(query, post.location, max_l_dist=3)  # Adjust max_l_dist as per your preference
            # if title_matches or location_matches:
                blogs.append(post)
    else:
        blogs = []

    return render(request, 'blog/search.html', {'blogs': blogs, 'query': query})
@login_required
def report_blog(request, blog_id):
    try:
        blog = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        url = reverse('catch_all_view')
        return redirect(url)
    slug = slugify(translate_hindi_to_english(blog.title))
    form = ReportForm()  # Initialize the form outside the if-else block

    if request.method == 'POST' and blog.user != request.user:
        form = ReportForm(request.POST)
        if form.is_valid():
            report_type = form.cleaned_data['report_type']
            reason = form.cleaned_data['reason']
            reporter = request.user
            report = Report(blog=blog, reporter=reporter, report_type=report_type, reason=reason)
            report.save()
            url = reverse('blog_details', kwargs={'title':slug, 'blog_id': blog_id})
            return redirect(url)

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog/report_blog.html', context)
