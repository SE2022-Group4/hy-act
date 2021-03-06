# Generated by Django 4.0.4 on 2022-06-04 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendancecode',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.program'),
        ),
        migrations.AddField(
            model_name='application',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.program'),
        ),
        migrations.AddField(
            model_name='application',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
