# Generated by Django 2.1 on 2018-10-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opticalcharacterrecognition',
            name='text_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
