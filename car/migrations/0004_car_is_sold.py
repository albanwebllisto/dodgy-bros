# Generated by Django 3.1.7 on 2021-03-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0003_remove_car_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="is_sold",
            field=models.BooleanField(default=False),
        ),
    ]
