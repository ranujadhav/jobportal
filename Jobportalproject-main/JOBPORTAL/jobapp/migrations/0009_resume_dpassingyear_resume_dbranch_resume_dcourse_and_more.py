# Generated by Django 4.0.2 on 2022-06-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0008_rename_educationqualification_resume_percentage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='dPassingyear',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='dbranch',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='dcourse',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='dpercentage',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AddField(
            model_name='resume',
            name='gPassingyear',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='gbranch',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='gcourse',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='gpercentage',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AddField(
            model_name='resume',
            name='pgPassingyear',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='pgbranch',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='pgcourse',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='pgpercentage',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]
