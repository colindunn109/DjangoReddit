from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import misaka


from django.contrib.auth import get_user_model
User = get_user_model()


from django import template
register = template.Library()


class Subreddit(models.Model):
    name = models.CharField(max_length=128,unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='SubMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('subs:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class SubMember(models.Model):
    sub = models.ForeignKey(Subreddit,related_name='memberships',on_delete="CASCADE")
    user = models.ForeignKey(User,related_name='user_subs',on_delete="CASCADE")

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('sub','user')
