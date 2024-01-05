from django.forms import DateInput
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author


class PostFilter(FilterSet):
    datetime = DateFilter(
        field_name='datetime',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='date__gte',
        label='Дата'
    )
    header = CharFilter(
        field_name='header',
        lookup_expr='icontains',
        label='Название заголовка'
    )
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Все'
    )

    class Meta:
        model = Post
        fields = [
            'header',
            'author',
            'datetime'
        ]