# Generated by Django 3.0.10 on 2021-05-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='OR  upload the thumbnail'),
        ),
    ]
