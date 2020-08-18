# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from sympy import sympify, latex

from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the Automath index.")


def detail(request, titre):
    question = get_object_or_404(Question, pk=titre)
    enonce = question.enonce
    dico_questions = {}
    nbe_questions = 10
    while len(dico_questions) != nbe_questions:
        loc = {}
        exec(enonce, globals(), loc)
        affichage = loc['affichage']
        # Affichage style LaTeX sans evaluation du texte initial
        affichage = latex(sympify(affichage, evaluate=False), mul_symbol='times')
        resultat = loc['resultat']
        resultat = latex(sympify(resultat), mul_symbol='times')
        dico_questions[affichage] = resultat
    # loc : dictionnaire des variables locales de exec
    # print(loc)
    return render(request,
                  'automath/detail.html',
                  {'dico_questions': dico_questions, 'question': question.question}
                  )


# from .forms import ConfigForm
from .forms import ProductFilter


# def get_config(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ConfigForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ConfigForm()
#
#     return render(request, 'automath/config.html', {'form': form})

def get_config(request):
    f = ProductFilter(request.GET, queryset=Question.objects.all())
    return render(request, 'automath/config.html', {'filter': f})
