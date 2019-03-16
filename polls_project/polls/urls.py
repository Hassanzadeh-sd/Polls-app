from django.conf.urls import url
from . import views

app_name= "polls"

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.list_view),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail_view, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote', views.vote , name='vote')
]
