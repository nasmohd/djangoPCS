# Generated by Django 3.1.5 on 2021-12-26 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PCS_system', '0004_project_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(default='x', on_delete=django.db.models.deletion.CASCADE, to='PCS_system.student'),
        ),
    ]
