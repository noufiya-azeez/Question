# from django.urls import path
# from . import views

# urlpatterns = [
#     path('index/',views.index,name='index'),
# ]

from django.urls import path,include

from . import views

urlpatterns = [
    # # ex: /polls/
    # # path('index/', views.index,name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('myapp/',views.Question_list,name='question_list'),
    path('myapp/question/int:pk>/',views.Choice_list,name='Choice_list')
]