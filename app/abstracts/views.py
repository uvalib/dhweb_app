from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.db.models import Count, Max, Min
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import (
    Version,
    Work,
    Author,
    Conference,
    Institution,
    Gender,
    Appellation,
    Department,
    ConferenceSeries,
)


class WorkList(ListView):
    context_object_name = "work_list"
    template_name = "index.html"

    def get_queryset(self):
        return Work.objects.all()[:10]


class WorkView(DetailView):
    model = Work
    template_name = "work_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        # Add in a QuerySet of all the books
        context["work_versions"] = obj.versions.all()
        context["work_authors"] = obj.versions.first().authors.all()
        return context


class AuthorView(DetailView):
    model = Author
    template_name = "author_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()

        context["authored_works"] = Work.objects.filter(
            versions__authors=obj
        ).distinct()

        context["appellations"] = obj.appellations.distinct()

        context["genders"] = obj.genders.distinct()

        context["departments"] = obj.departments.distinct()

        context["institutions"] = obj.institutions.distinct()

        context["authored_versions"] = obj.versions.distinct().order_by(
            "-work__conference__year"
        )

        context["institution_choices"] = Institution.objects.order_by("name")

        context["gender_choices"] = Gender.objects.order_by("?")

        return context


class AuthorList(ListView):
    context_object_name = "author_list"
    template_name = "author_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.annotate(
            last_name=Max("appellations__last_name")
        ).order_by("last_name")


class ConferenceView(DetailView):
    model = Conference
    template_name = "conference_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        context["works"] = obj.works.all()
        return context


class ConferenceList(ListView):
    context_object_name = "conference_list"
    template_name = "conference_list.html"

    def get_queryset(self):
        return Conference.objects.order_by("-year")


class SeriesList(ListView):
    context_object_name = "series_list"
    template_name = "series_list.html"

    def get_queryset(self):
        return ConferenceSeries.objects.order_by("title")


class SeriesView(DetailView):
    model = ConferenceSeries
    template_name = "series_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        context["conferences"] = obj.conferences.order_by("series_memberships__number")
        return context


class InstitutionView(DetailView):
    model = Institution
    template_name = "institution_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        context["members"] = obj.members.distinct()
        return context


class InstitutionList(ListView):
    context_object_name = "institution_list"
    template_name = "institution_list.html"

    def get_queryset(self):
        return Institution.objects.annotate(
            num_members=Count("members", distinct=True)
        ).order_by("-num_members")


def home_view(request):
    conference_count = Conference.objects.count()
    work_count = Work.objects.count()
    author_count = Author.objects.count()
    institution_count = Institution.objects.count()
    country_count = Institution.objects.values("country").distinct().count()
    context = {
        "conference_count": conference_count,
        "work_count": work_count,
        "author_count": author_count,
        "institution_count": institution_count,
        "country_count": country_count,
    }
    return render(request, "index.html", context)
