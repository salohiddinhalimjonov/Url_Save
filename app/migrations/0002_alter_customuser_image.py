# Generated by Django 3.2.4 on 2021-08-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='/images/resume.png', null=True, upload_to='images/'),
        ),
    ]
