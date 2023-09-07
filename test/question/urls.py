from django.urls import path
from .views import (GroupListView, SetListView,
                    question_view, question_from_view, res)

app_name = 'question'

urlpatterns = [
     path('', SetListView.as_view(), name='set_list'),
     path('result/', res, name='result'),
     path('<slug:group_name>/<int:pk>/', question_from_view,
          name='question'),
     path('<slug:set_name>/', GroupListView.as_view(), name='group_list'),
     path('<slug:set_name>/<slug:group_name>/', question_view,
          name='desc_test'),
]
