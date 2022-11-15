from django.shortcuts import render
from django.http import HttpResponse,Http404
from . models import Question

# Create your views here.


# def index(request):
#     return HttpResponse("Hello World")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


def Question_list(request):
    questions = Question.objects.all()
    return render(request,'myapp2/question_list.html',{'questions':questions})


def Choice_list(request,pk):
    question =Question.objects.get(pk=pk)
    return render(request,'myapp2/choice_list.html',{'question':question})