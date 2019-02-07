from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    url(r'^by/(?p<username>[-\w]+)',views.UserPosts.as_view(),name='for_user'),
    url(r'^by/(?p<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    path('delete/<pk>',views.DeletePost.as_view(),name='delete')
]
