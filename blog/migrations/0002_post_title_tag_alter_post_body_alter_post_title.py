# Generated by Django 4.0.3 on 2022-05-03 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog...', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
