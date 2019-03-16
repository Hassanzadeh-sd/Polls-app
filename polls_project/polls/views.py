from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from . import models
from django.urls import reverse

def list_view(request):
    q = models.Question.objects.all()
    context = {'latest_question_list' : q}
    return render(request,'polls/question_view.html' , context)

def detail_view(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'polls/question_choics.html' , {'question':question})

def results(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request ,'polls/question_results.html' , {'question':question})

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except Exception as e:
        return render(request , 'polls/question_choics.html' , {
            'question' : question ,
            'error_message' : "you didn't select a choice.",
        })

    selected_choice.vote += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
