# Generated by Django 3.2.7 on 2021-09-18 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0008_auto_20210918_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='studentInClass',
            field=models.ManyToManyField(blank=True, related_name='studentlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
