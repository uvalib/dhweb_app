from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("works", views.WorkList.as_view(), name="work_list"),
    path("works/<int:pk>", views.WorkView.as_view(), name="work_detail"),
    path("authors", views.AuthorList.as_view(), name="author_list"),
    path("authors/<int:pk>", views.AuthorView.as_view(), name="author_detail"),
    path("authors/merge/<int:author_id>", views.author_merge_view, name="author_merge"),
    path("conferences", views.ConferenceList.as_view(), name="conference_list"),
]
