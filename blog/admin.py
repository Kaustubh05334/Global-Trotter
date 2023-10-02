from django.contrib import admin
from .models import BlogPost,SubBlogPost,Comment,AdminComment,Report
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(SubBlogPost)
admin.site.register(Comment)
admin.site.register(AdminComment)
admin.site.register(Report)
