# Generated by Django 4.0.4 on 2022-06-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_departments_alter_user_majors'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='real_name',
            field=models.CharField(default='홍길동', max_length=150, verbose_name="User's real name"),
            preserve_default=False,
        ),
    ]
