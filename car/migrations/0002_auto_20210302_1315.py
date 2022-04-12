# Generated by Django 3.1.7 on 2021-03-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="user",
        ),
        migrations.AddField(
            model_name="car",
            name="seller_mobile",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="car",
            name="seller_name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
