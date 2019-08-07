from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from slugify import slugify

from . import forms
from . import models


class BlogCreateView(CreateView):
    model = models.Entry
    template_name = "blog/blog_new.html"
    form_class = forms.BlogForm

    def post(self, request, *args, **kwargs):
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = "Paul Jenkins"
            post.slug = slugify(post.title)
            post.save()
            return HttpResponseRedirect(reverse('blog:blog-detail', kwargs={'slug': post.slug}))
        else:
            form = forms.BlogForm()
        return render(request, 'blog/blog_new.html', {'form': form})


class BlogUpdateView(UpdateView):
    model = models.Entry
    template_name = "blog/blog_new.html"


class BlogListView(TemplateView):
    model = models.Entry
    template_name = "blog/blog_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = models.Entry.objects.all()
        return context


class BlogDetailView(TemplateView):
    model = models.Entry
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = models.Entry.objects.all()
        context['blog'] = models.Entry.objects.get(slug=kwargs['slug'])
        return context
