# Generated by Django 2.0.5 on 2018-05-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_extendedprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_author_id',
            field=models.IntegerField(default=-1),
        ),
    ]
