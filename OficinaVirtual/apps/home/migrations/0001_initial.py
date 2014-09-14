# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import OficinaVirtual.apps.home.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('photo', models.ImageField(upload_to=OficinaVirtual.apps.home.models.userProfile.url)),
                ('telefono', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
