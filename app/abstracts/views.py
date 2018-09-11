from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Version, Tag, Work, Author, SubmissionEvent

class TagView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'

class TagList(ListView):
    context_object_name = 'tag_list'
    template_name = 'tag_list.html'

    def get_queryset(self):
        return Tag.objects.all()

class WorkList(ListView):
    context_object_name = 'work_list'
    template_name = 'index.html'

    def get_queryset(self):
        return Work.objects.all()[:10]

class WorkView(DetailView):
    model = Work
    template_name = 'work_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        # Add in a QuerySet of all the books
        context['work_versions'] = obj.versions.all()
        context['work_authorships'] = obj.versions.first().authorships.order_by("authorship_order")
        return context

class AuthorView(DetailView):
    model = Author
    template_name = 'author_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        context['authored_works'] = Work.objects.filter(
            versions__authorships__author=obj).distinct
        context['appellations'] = obj.appellations.all()
        context['gender_memberships'] = obj.gender_memberships.all()
        context['department_memberships'] = obj.department_memberships.all()
        context['institution_memberships'] = obj.institution_memberships.all()
        return context

class AuthorList(ListView):
    context_object_name = 'author_list'
    template_name = 'author_list.html'

    def get_queryset(self):
        return Author.objects.all()

class SubmissionView(DetailView):
    model = SubmissionEvent
    template_name = 'submission_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        context['works'] = obj.works.all()
        return(context)

class SubmissionList(ListView):
    context_object_name = 'submission_list'
    template_name = 'submission_list.html'

    def get_queryset(self):
        return SubmissionEvent.objects.order_by("year")
