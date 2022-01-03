from django.contrib import admin

from .models import Author, Post, Publisher


from django.contrib.admin.sites import AdminSite
from django.urls import path

from .views import HomeView


class DashboardSite(AdminSite):
    def get_urls(self):
        urls = super(DashboardSite , self).get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(HomeView.as_view()), name='index'),
        ]

        return custom_urls + urls




# ===================================
# class BlogAdminArea(admin.AdminSite):
#     site_header = 'Blog Admin'


# class TestBlogAdminPermission(admin.ModelAdmin):
    
#     def has_add_permission(self, request):
#         return False

# blog_admin_site = BlogAdminArea(name='BlogAdmin')

# blog_admin_site.register(Author)
# blog_admin_site.register(Publisher)
# blog_admin_site.register(Post, TestBlogAdminPermission)



# ===================================
# admin.site.register(Author)
# admin.site.register(Publisher)
# admin.site.register(Post)