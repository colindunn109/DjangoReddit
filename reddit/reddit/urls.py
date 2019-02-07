from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('subreddit/',include('subreddits.urls',namespace='subs')),
    path('posts/',include('subreddits.urls',namespace='posts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
]
