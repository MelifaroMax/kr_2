# Generated by Django 5.1.7 on 2025-05-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='page_images/'),
        ),
    ]
