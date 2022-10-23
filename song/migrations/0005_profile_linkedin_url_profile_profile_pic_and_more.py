# Generated by Django 4.1.2 on 2022-10-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]