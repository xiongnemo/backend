# Generated by Django 3.1.2 on 2020-12-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announcement_id', models.AutoField(primary_key=True, serialize=False)),
                ('announcement_title', models.CharField(max_length=50)),
                ('announcement_contents', models.CharField(max_length=1024, null=True)),
                ('announcement_is_pinned', models.BooleanField(default=False)),
                ('announcement_publish_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
