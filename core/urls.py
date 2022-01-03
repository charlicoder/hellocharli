from django.contrib import admin
from django.urls import path, include
# from graphene_django.views import GraphQLView
# from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

# from blog.admin import blog_admin_site

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('blogadmin/', blog_admin_site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    
    # path('signin/', TemplateView.as_view(template_name="auth-signin.html"), name='signin'),
    # path('signup/', TemplateView.as_view(template_name="auth-signup.html"), name='signup'),
    # path("", include("aaa.urls")),
    # path("accounts/", include("accounts.urls")),
    path("books/", include("bookstore.urls")),

    # path('citizens/', TemplateView.as_view(template_name="tbl_bootstrap.html"), name='citizens'),
    # path('villages/', TemplateView.as_view(template_name="map-google.html"), name='villages'),
]


admin.site.site_header = 'Hello Charli'
