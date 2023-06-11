# Generated by Django 4.2.2 on 2023-06-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Man", "Man"),
                            ("Woman", "Woman"),
                            ("Unisex", "Unisex"),
                        ],
                        max_length=6,
                        verbose_name="gender",
                    ),
                ),
                ("size", models.CharField(max_length=50, verbose_name="size")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            (
                                "Clothes",
                                (
                                    ("Shirt", "Shirt"),
                                    ("Joggers", "Joggers"),
                                    ("Hoodies", "Hoodies"),
                                    ("Shorts", "Shorts"),
                                    ("Jeans", "Jeans"),
                                ),
                            ),
                            (
                                "Shoes",
                                (
                                    ("Sneakers", "Sneakers"),
                                    ("Slates", "Slates"),
                                    ("Sandals", "Sandals"),
                                    ("Boots", "Boots"),
                                    ("Loafers", "Loafers"),
                                    ("Slippers", "Slippers"),
                                ),
                            ),
                        ],
                        max_length=50,
                        verbose_name="type",
                    ),
                ),
                ("price", models.FloatField(verbose_name="price")),
                (
                    "image",
                    models.ImageField(blank=True, upload_to=None, verbose_name="image"),
                ),
                (
                    "description",
                    models.CharField(max_length=300, verbose_name="description"),
                ),
                (
                    "composition",
                    models.CharField(max_length=100, verbose_name="composition"),
                ),
                (
                    "collection",
                    models.CharField(max_length=20, verbose_name="collection"),
                ),
            ],
        ),
    ]
