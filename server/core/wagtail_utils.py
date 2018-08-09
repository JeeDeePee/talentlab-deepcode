from django.contrib import admin


def wagtail_parent_filter(parent_cls, child_cls):
    class ParentValueFilter(admin.SimpleListFilter):
        title = 'parent'
        parameter_name = 'parent'

        def lookups(self, request, model_admin):
            return list((parent.slug, parent.title) for parent in parent_cls.objects.all())

        def queryset(self, request, queryset):
            filter_value = self.value()
            parent = parent_cls.objects.filter(slug=filter_value).first()
            if parent:
                return child_cls.objects.filter(id__in=parent.get_child_ids()).live()

    return ParentValueFilter
