# Generated by Django 3.1.2 on 2020-12-20 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('homework_teachers_comments', models.CharField(max_length=2048)),
                ('homework_is_grade_available_to_students', models.BooleanField(default=False)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseChapterDescrption',
            fields=[
                ('course_chapter_description_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.IntegerField()),
                ('course_chapter_id', models.IntegerField()),
                ('course_chapter_title', models.CharField(max_length=64)),
                ('course_chapter_mooc_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('homework_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.IntegerField()),
                ('homework_creator', models.IntegerField()),
                ('homework_title', models.CharField(max_length=128)),
                ('homework_description', models.CharField(max_length=1024)),
                ('homework_start_timestamp', models.DateTimeField()),
                ('homework_end_timestamp', models.DateTimeField()),
                ('homework_create_timestamp', models.DateTimeField()),
                ('homework_update_timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkFile',
            fields=[
                ('file_homework_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_display_name', models.CharField(max_length=1024)),
                ('file_comment', models.CharField(max_length=1024)),
                ('file_uploader', models.IntegerField()),
                ('file_timestamp', models.DateField(auto_now=True)),
                ('file_token', models.CharField(max_length=200)),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lecture.homework')),
            ],
        ),
    ]
