# Generated by Django 4.2.7 on 2024-07-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_visited', models.CharField(max_length=255, unique=True)),
                ('visit_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
