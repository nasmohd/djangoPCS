# Generated by Django 3.1.5 on 2021-12-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PCS_system', '0006_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_description', models.CharField(max_length=800)),
                ('project_partners', models.CharField(max_length=10)),
                ('project_budget', models.CharField(max_length=20)),
                ('project_image', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(default='x', on_delete=django.db.models.deletion.CASCADE, to='PCS_system.student')),
            ],
        ),
    ]
