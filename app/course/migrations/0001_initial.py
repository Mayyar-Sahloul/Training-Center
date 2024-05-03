# Generated by Django 3.2.23 on 2024-01-12 20:15

import course.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('image', models.ImageField(blank=True, default='', upload_to=course.models.image_file_path)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Courses', to='teacher.teacher')),
                ('tags', models.ManyToManyField(to='course.Tag')),
            ],
        ),
    ]