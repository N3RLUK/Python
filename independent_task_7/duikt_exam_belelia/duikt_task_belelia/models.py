from django.db import models

class cars_brand(models.Model):
    BRAND_NAME = models.CharField(max_length=100)
    BRAND_COUNTRY = models.CharField(max_length=100)
    BRAND_RATING = models.IntegerField()

    def __str__(self):
        return self.BRAND_NAME

class cars_info(models.Model):
    CAR_NAME = models.CharField(max_length=100)
    CAR_MODEL = models.CharField(max_length=100)
    CAR_PRICE = models.FloatField()
    CAR_BRAND = models.ForeignKey(cars_brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.CAR_NAME
