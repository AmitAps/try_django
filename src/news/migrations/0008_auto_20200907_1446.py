# Generated by Django 2.2 on 2020-09-07 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200907_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish_date', '-timestamp', '-updated']},
        ),
    ]
