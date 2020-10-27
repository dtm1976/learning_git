# Generated by Django 3.1.2 on 2020-10-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('publish', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
