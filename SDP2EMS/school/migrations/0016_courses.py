# Generated by Django 3.0.5 on 2021-05-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_delete_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=50)),
                ('coursecode', models.CharField(max_length=20)),
                ('credits', models.CharField(max_length=10)),
                ('handoutfilename', models.CharField(max_length=50)),
            ],
        ),
    ]