# Generated by Django 3.2.5 on 2021-08-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_challenge_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='period',
        ),
        migrations.AddField(
            model_name='challenge',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
