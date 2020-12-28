from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect # HttpResponse, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")

#     # Equivalent to comment block above
#     question = get_object_or_404(Question, pk=question_id)
#     # get_list_or_404() works similarily but uses filter() instead of get()

#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# Using generic views instead of comment block above
class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    # Override context variable name, `question_list`
    context_object_name = 'latest_question_list'

    # Get the list of items for this view
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # What model the generic view will be acting upon
    # Model is provided automatically to html file:
    # (model=Question, name=question, pk=question_id)
    model = Question

    # specify so that different classes use different templates
    # or all classes using DetailView use template <app name>/<model name>_detail.html
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # get posted data with name `choice`, raises KeyError if choice wasn't provided
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # Reverse will return a string like "/polls/3/results/"
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))