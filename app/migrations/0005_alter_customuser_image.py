# Generated by Django 3.2.4 on 2021-08-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='images/image1.jpg', null=True, upload_to='images/'),
        ),
    ]