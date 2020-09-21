# Generated by Django 3.1.1 on 2020-09-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200, null=True)),
                ('description', models.TextField(default=None, max_length=1000, null=True)),
                ('video', models.FileField(null=True, upload_to='video_files')),
                ('images', models.ImageField(upload_to='videos')),
                ('code', models.CharField(default=None, max_length=20, null=True)),
                ('create_at', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]
