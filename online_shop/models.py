from django.db import models

TYPE_CHOICES = (
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
        )
    ),
)

GENDER_CHOICES = (
    ("Man", "Man"),
    ("Woman", "Woman"),
    ("Unisex", "Unisex"),
)

SIZE_CHOICES = (
    (
        "Clothes",
        (
            ("S", "S"),
            ("XS", "XS"),
            ("M", "M"),
            ("L", "L"),
            ("XL", "XL"),
        ),
    ),
    (
        "Shoes",
        (
            ("40", "40"),
            ("41", "41"),
            ("42", "42"),
            ("43", "43"),
            ("44", "44"),
            ("45", "45"),
        )
    ),
)

# Create your models here.
class Product(models.Model):
    gender = models.CharField(("gender"), choices=GENDER_CHOICES, max_length=6)
    size = models.CharField(("size"), max_length=50)
    type = models.CharField(("type"), choices=TYPE_CHOICES, max_length=50)
    price = models.FloatField(("price"))
    image = models.ImageField(("image"), upload_to=None, blank=True)
    description = models.CharField(("description"), max_length=300)
    composition = models.CharField(("composition"), max_length=100)
    collection = models.CharField(("collection"), max_length=20)
    
    def __str__(self):
        return self.name