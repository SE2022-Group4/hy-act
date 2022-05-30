# Generated by Django 4.0.4 on 2022-05-26 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_rename_class_end_at_program_program_end_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='max_applicant_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='program',
            name='target_grade',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='target_major',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='thumbnail_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
