import django_filters

from .models import Question


# class ConfigForm(forms.Form):
#     titre_question = forms.ModelChoiceField(queryset=Question.objects.all())
#     # titre_question = forms.ChoiceField(choices=Question.Themes.choices)


class ProductFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(lookup_expr='icontains', )

    class Meta:
        model = Question
        fields = ['theme', 'niveau']
