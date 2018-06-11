from querysys.models import user
import django_filters

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = user
        fields = ['username', 'first_name', 'last_name', ]
