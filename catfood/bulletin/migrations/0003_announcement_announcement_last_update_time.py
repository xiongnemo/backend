# Generated by Django 3.1.2 on 2020-12-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0002_auto_20201124_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='announcement_last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
