# Generated by Django 3.2.7 on 2021-09-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_auto_20210917_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='status',
            field=models.CharField(choices=[('free', 'Free'), ('full', 'Full')], default='free', max_length=4),
        ),
    ]
