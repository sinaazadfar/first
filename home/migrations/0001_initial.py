# Generated by Django 3.1.3 on 2020-11-15 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(max_length=600)),
                ('image', models.ImageField(upload_to='images')),
                ('published', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'published')], max_length=1)),
            ],
        ),
    ]
