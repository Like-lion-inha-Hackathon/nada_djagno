# Generated by Django 3.2.5 on 2021-08-09 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_alter_challenge_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='category',
            field=models.CharField(choices=[('study', 'Study'), ('reading', 'Reading'), ('hobby', 'Hobby'), ('health', 'Health'), ('habbit', 'Habbit'), ('work', 'Work')], max_length=30, null=True),
        ),
    ]
