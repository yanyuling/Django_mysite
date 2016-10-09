from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userLogin/$', views.userLogin, name='userLogin'),
    # url(r'^userLogin2/(?P<username>\w+)&(?P<password>\w+)$', views.userLogin2, name='userLogin2'),
    url(r'^userRegister/$', views.userRegister, name='userRegister'),


    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]

# """
#     cfg:        url(r'^userLogin2/(?P<username>\w+)&(?P<password>\w+)$', views.userLogin2, name='userLogin2'),
#     req:        http://127.0.0.1:8000/polls/userLogin2/asdf&11111
#     FunDeal:    def userLogin2(request,username,password):

#     cfg:        url(r'^userLogin/$', views.userLogin, name='userLogin'),
#     req:        http://127.0.0.1:8000/polls/userLogin/?username=yanyuling&password=111111
#     FunDeal:    def userLogin(request):
#                     username=request.GET.get('username','')
#                     password=request.GET.get('password','')



# """