# Generated by Django 5.0.1 on 2024-02-10 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0002_tbl_user'),
        ('User', '0008_delete_tbl_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.CharField(max_length=30)),
                ('hour', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_user')),
            ],
        ),
    ]
