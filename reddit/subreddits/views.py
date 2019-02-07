from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from subreddits.models import Subreddit, SubMember

class CreateSubreddit(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Subreddit

class SingleSub(generic.DetailView):
    model = Subreddit

class ListSubs(generic.ListView):
    model = Subreddit

class JoinSubreddit(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('subs:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        sub = get_object_or_404(Subreddit,slug=self.kwargs.get('slug'))
        try:
            SubMember.objects.create(user=self.request.user,sub=sub)
        except IntegrityError:
            messages.warning(self.request,'Already a member!')
        else:
            messages.success(self.request,'You are now a member!')

        return super().get(request,*args,**kwargs)

class LeaveSubreddit(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('subs:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership = models.SubMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except models.SubMember.DoesNotExist:
            messages.warning(self.request,'Sorry, you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group!')

        return super().get(request,*args,**kwargs)
