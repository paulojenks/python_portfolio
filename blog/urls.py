from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name="blog-home"),
    url(r'new/$', views.BlogCreateView.as_view(), name="blog-new"),
    url(r'(?P<slug>\S+)/update/$', views.BlogUpdateView.as_view(), name="blog-update"),
    url(r'(?P<slug>\S+)/$', views.BlogDetailView.as_view(), name="blog-detail"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)