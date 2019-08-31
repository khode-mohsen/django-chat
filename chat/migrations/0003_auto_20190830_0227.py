# Generated by Django 2.2.4 on 2019-08-29 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_room_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='staff_only',
        ),
        migrations.RemoveField(
            model_name='room',
            name='title',
        ),
        migrations.RemoveField(
            model_name='room',
            name='users',
        ),
        migrations.AddField(
            model_name='room',
            name='allow_anonymous_access',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=0, max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='room',
            name='private',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='subscribers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('content', models.CharField(max_length=5000)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
