import django_filters

from core.middleware import get_current_user


def graphql_user_filter(model_cls, filter_fields):
    class UserFilter(django_filters.FilterSet):
        class Meta:
            model = model_cls
            fields = filter_fields

        @property
        def qs(self):
            user = get_current_user()
            if not user:
                return model_cls.objects.none()
            return super(UserFilter, self).qs.filter(user=user)

    return UserFilter
