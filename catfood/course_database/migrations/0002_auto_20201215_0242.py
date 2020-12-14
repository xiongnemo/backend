# Generated by Django 3.1.2 on 2020-12-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursedocument',
            old_name='file_timestamp',
            new_name='file_create_timestamp',
        ),
        migrations.RenameField(
            model_name='coursedocument',
            old_name='file_link',
            new_name='file_token',
        ),
        migrations.RemoveField(
            model_name='coursedocument',
            name='file_usage',
        ),
        migrations.AddField(
            model_name='coursedocument',
            name='course_id',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursedocument',
            name='file_display_name',
            field=models.CharField(default='PPP', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursedocument',
            name='file_update_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='coursedocument',
            name='file_uploader',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
