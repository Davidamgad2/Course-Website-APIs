# Generated by Django 4.1 on 2022-10-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ManyToManyField(to='Course.instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='reviews',
            field=models.ManyToManyField(to='Course.review'),
        ),
    ]
