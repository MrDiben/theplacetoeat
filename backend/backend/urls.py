from django.urls import path
from django.utils.translation import gettext as _

from backend import admin

from .api_urls import urlpatterns as apiurlpatterns

admin.site.site_title = "Backend"
admin.site.site_header = "Backend"
admin.site.site_url = None
admin.site.index_title = _("Dashboard")


urlpatterns = [path("admin/", admin.site.urls)]

urlpatterns += apiurlpatterns
