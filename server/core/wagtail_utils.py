from django.contrib import admin
from wagtail.core.models import Page


class StrictHierarchyPage(Page):
    class Meta:
        abstract = True

    def get_child_ids(self):
        return self.get_children().values_list('id', flat=True)

    @classmethod
    def get_by_parent(cls, parent):
        return cls.objects.filter(id__in=parent.get_child_ids()).live()


def wagtail_parent_filter(parent_cls, child_cls):
    class ParentPageFilter(admin.SimpleListFilter):
        title = 'parent'
        parameter_name = 'parent'

        def lookups(self, request, model_admin):
            return list((parent.slug, parent.title) for parent in parent_cls.objects.all())

        def queryset(self, request, queryset):
            filter_value = self.value()
            parent = parent_cls.objects.filter(slug=filter_value).first()
            if parent:
                return child_cls.objects.filter(id__in=parent.get_child_ids()).live()

    return ParentPageFilter
