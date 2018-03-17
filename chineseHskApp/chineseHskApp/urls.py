from django.conf.urls import include, url
from django.contrib import admin
from hskHelper import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'chineseHskApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^timedQuestions/$', views.timedQuestionsPage, name='timedquestions'),
    url(r'^speedVocab/$', views.speedVocabPage, name='speedvocab'),
    url(r'^speedWriting/$', views.speedWritingPage, name='speedwriting'),
]
