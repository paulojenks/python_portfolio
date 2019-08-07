from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from portfolio import views

app_name="portfolio"
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'about/$', views.ProfileView.as_view(), name="profile"),
    url(r'projects/$', views.ProjectListView.as_view(), name="projects"),
    url(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name="project"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

