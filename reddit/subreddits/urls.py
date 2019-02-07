from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'subs'

urlpatterns = [
    path('',views.ListSubs.as_view(),name='all'),
    path('new/',views.CreateSubreddit.as_view(),name='create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$',views.SingleSub.as_view(),name='single'),
    url(r'^join/(?P<slug>[-\w]+)/$',views.JoinSubreddit.as_view(),name='join'),
    url(r'^leave/(?P<slug>[-\w]+)/$',views.LeaveSubreddit.as_view(),name='leave'),

]
