from django.shortcuts import render
from django.views.generic import TemplateView


from . import models


# Home page, no need for class view, no model used on this page
def home(request):
    return render(request, 'portfolio/home.html')


# ProfileView- TemplateView- class view, used Profile model to show user profile info
class ProfileView(TemplateView):
    model = models.Profile
    template_name = 'portfolio/about-me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = models.Profile.objects.get(first_name=kwargs['name'])
        return context


# Projects home page- model used to build navigation menu of all projects created
class ProjectListView(TemplateView):
    model = models.Project
    template_name = 'portfolio/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = models.Project.objects.all()
        return context


# Project Detail page display particular project- projects used for navigation menu
class ProjectDetailView(TemplateView):
    model = models.Project
    template_name = 'portfolio/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = models.Project.objects.get(pk=kwargs['pk'])
        context['projects'] = models.Project.objects.all()
        return context



