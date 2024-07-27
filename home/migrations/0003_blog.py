# Generated by Django 5.0.6 on 2024-07-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('blog_id', models.CharField(max_length=100)),
                ('head_title', models.CharField(max_length=200)),
                ('title1', models.TextField()),
                ('title2', models.TextField(blank=True)),
                ('title3', models.TextField(blank=True)),
                ('img1', models.TextField(blank=True)),
                ('img2', models.TextField(blank=True)),
                ('img3', models.TextField(blank=True)),
                ('content1', models.TextField()),
                ('content2', models.TextField(blank=True)),
                ('content3', models.TextField(blank=True)),
                ('keyword1', models.CharField(max_length=100)),
                ('keyword2', models.CharField(blank=True, max_length=100)),
                ('keyword3', models.CharField(blank=True, max_length=100)),
                ('time_stamp', models.DateField()),
            ],
        ),
    ]