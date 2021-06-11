
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from src.apps.core.views import PersonCreateView, ListView, MatchView


urlpatterns = [
    path("admin/", admin.site.urls),

    path("create", PersonCreateView.as_view(), name="create"),
    path("list", ListView.as_view(), name="list"),
    path("match", MatchView.as_view(), name="match"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
