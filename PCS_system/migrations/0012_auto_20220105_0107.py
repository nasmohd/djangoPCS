# Generated by Django 3.1.5 on 2022-01-04 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PCS_system', '0011_auto_20220102_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='role_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='PCS_system.role'),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=500)),
                ('role_id', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='PCS_system.role')),
            ],
        ),
    ]
