# Generated by Django 4.0.6 on 2022-07-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_videos_payment_alter_videos_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='length',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]