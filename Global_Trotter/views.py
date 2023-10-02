from django.shortcuts import render,redirect,get_object_or_404
from blog.models import BlogPost,Report
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
def homepage(request):
    return render(request, 'homeblog.html')


def Packages(request):
    return render(request, 'packages.html')

@login_required(login_url='login_page')
def blog_approval(request):
    if request.user.is_superuser:
        posts = BlogPost.objects.filter(status=0)
    else:
        url = reverse('catch_all_view')
        return redirect(url)
    return render(request,'admin/approval.html',{'posts':posts})

def catch_all_view(request):
    return render(request,'404.html')

@login_required
def blog_reports(request):
    if not request.user.is_superuser:
        url = reverse('catch_all_view')
        return redirect(url)
    reports = Report.objects.filter(resolved_status=False)
    
    if request.method == 'POST':
        selected_option = request.POST.get('my_select')
        if selected_option != "all":
            reports = reports.filter(report_type=selected_option)
    context={
        "reports":reports
    }
    return render(request, 'admin/report.html',context)

@login_required
def unique_report(request,report_id):
    if not request.user.is_superuser:
        url = reverse('catch_all_view')
        return redirect(url)
    report = get_object_or_404(Report,id=report_id)
    if request.method=="POST":
        rid= request.POST.get('report_id')
        report = get_object_or_404(Report,id=rid)
        report.resolved_status=True
        report.save()
        print(report.resolved_status)
        url = reverse('reports_list')
        return redirect(url)
    return render(request,'admin/unique_report.html',{'report':report})

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            # Update the user's password
            user.set_password(password)
            user.save()

            # Redirect to the home page
            return redirect('home')
        else:
            # Passwords don't match
            return render(request, 'change_password.html', {'user': user, 'error': 'Passwords do not match'})
    return render(request, 'change_password.html', {'user': user})

def hotel(request):
    blogs = BlogPost.objects.filter(category='hotels',status=1).order_by('-created_at')
    return render(request, 'common.html',{'head':'Hotels','blogs':blogs})

def airline(request):
    blogs = BlogPost.objects.filter(category='airline',status=1).order_by('-created_at')
    return render(request, 'common.html',{'head':'Airline','blogs':blogs})

def travel(request):
    blogs = BlogPost.objects.filter(category='travel',status=1).order_by('-created_at')
    return render(request, 'common.html',{'head':'Travel','blogs':blogs})

def lifestyle(request):
    blogs = BlogPost.objects.filter(category='lifestyle',status=1).order_by('-created_at')
    return render(request, 'common.html',{'head':'LifeStyle','blogs':blogs})

