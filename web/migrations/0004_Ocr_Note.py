# Generated by Django 3.2.7 on 2021-12-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_Ocr_Note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocr_note',
            name='ocr_pic',
            field=models.ImageField(blank=True, default='ProfilePicture.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ocr_note',
            name='ocr_text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]