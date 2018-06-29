# Generated by Django 2.0.6 on 2018-06-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binary', '0002_moduleobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=256, unique=True)),
                ('type', models.CharField(max_length=32)),
                ('module_1_id', models.IntegerField()),
                ('module_2_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('failed_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'module_results',
            },
        ),
    ]
