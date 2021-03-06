# Generated by Django 3.1.7 on 2021-03-02 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("make", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("year", models.DateTimeField()),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("poor", "Poor"),
                            ("fair", "Fair"),
                            ("good", "Good"),
                            ("excellent", "Excellent"),
                        ],
                        db_index=True,
                        default="good",
                        max_length=255,
                    ),
                ),
                ("price", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller",
                        to="core.userdetail",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
