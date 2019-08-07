from django.shortcuts import render
from django.views.generic import TemplateView


from . import models


def home(request):
    return render(request, 'portfolio/home.html')


class ProfileView(TemplateView):
    model = models.Profile
    template_name = 'portfolio/about-me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = models.Profile.objects.get(user=self.request.user)
        return context


class ProjectListView(TemplateView):
    model = models.Project
    template_name = 'portfolio/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = models.Project.objects.all()
        return context


class ProjectDetailView(TemplateView):
    model = models.Project
    template_name = 'portfolio/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = models.Project.objects.get(pk=kwargs['pk'])
        context['projects'] = models.Project.objects.all()
        return context



