from django_filters import rest_framework as filters
from .models import Snippet

class SnippetFilter(filters.FilterSet):
    date_published = filters.DateFromToRangeFilter()

    class Meta:
        model = Snippet
        fields = ['date_published', 'department', 'owner', 'style', 'language', 'title', 'linenos' ]
