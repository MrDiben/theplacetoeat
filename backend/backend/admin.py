from django.apps import apps
from django.contrib import admin


class BackendSite(admin.AdminSite):
    pass


site = BackendSite()


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        searchable_fields = ["TextField", "CharField", "URLField"]
        self.search_fields = [
            field.name
            for field in model._meta.fields
            if field.__class__.__name__ in searchable_fields
        ]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
for model in models:
    admin_class = type("AdminClass", (ListAdminMixin, admin.ModelAdmin), {})
    try:
        site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
