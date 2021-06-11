
from django.contrib import admin
from django.urls import path

from src.apps.core.views import CreateView, ListView, MatchView


urlpatterns = [
    path("admin/", admin.site.urls),

    path("create/", CreateView.as_view(), name="create"),
    path("list/", ListView.as_view(), name="list"),
    path("match/", MatchView.as_view(), name="match"),
]
