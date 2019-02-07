# Generated by Django 2.0.7 on 2019-02-06 22:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('description_html', models.TextField(blank=True, default='', editable=False)),
                ('members', models.ManyToManyField(through='subreddits.SubMember', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='submember',
            name='sub',
            field=models.ForeignKey(on_delete='CASCADE', related_name='memberships', to='subreddits.Subreddit'),
        ),
        migrations.AddField(
            model_name='submember',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', related_name='user_subs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='submember',
            unique_together={('sub', 'user')},
        ),
    ]
