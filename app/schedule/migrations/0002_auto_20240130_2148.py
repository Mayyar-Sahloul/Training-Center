# Generated by Django 3.2.23 on 2024-01-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='coursetimes',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='day',
        ),
        migrations.AddField(
            model_name='schedule',
            name='friday',
            field=models.ManyToManyField(blank=True, related_name='friday_courses', to='schedule.CourseTime'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='monday',
            field=models.ManyToManyField(blank=True, related_name='monday_courses', to='schedule.CourseTime'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='saturday',
            field=models.ManyToManyField(blank=True, related_name='saturday_courses', to='schedule.CourseTime'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='sunday',
            field=models.ManyToManyField(blank=True, related_name='sunday_courses', to='schedule.CourseTime'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='thuresday',
            field=models.ManyToManyField(blank=True, related_name='thuresday_courses', to='schedule.CourseTime'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='tuesday',
            field=models.ManyToManyField(blank=True, related_name='tuesday_courses', to='schedule.CourseTime'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='wednesday',
            field=models.ManyToManyField(blank=True, related_name='wednesday_courses', to='schedule.CourseTime'),
        ),
    ]