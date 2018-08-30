import django_filters
from .models import Report

class ReportsFilter(django_filters.rest_framework.FilterSet):
    #模糊查询，其中'contains'代表区分大小写，'icontains'代表不区分大小写
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model=Report
        fields=['name']