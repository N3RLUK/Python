from django.http import HttpResponse
from django.shortcuts import render
from .models import cars_brand, cars_info

def install(request):
    output = ""

    brands = [
        {"BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9},
        {"BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8},
        {"BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9}
    ]

    cars = [
        {"CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford"},
        {"CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW"}
    ]

    for b in brands:
        obj, created = cars_brand.objects.get_or_create(
            BRAND_NAME=b["BRAND_NAME"],
            BRAND_COUNTRY=b["BRAND_COUNTRY"],
            BRAND_RATING=b["BRAND_RATING"]
        )
        if created:
            output += f"Created brand: {obj.BRAND_NAME}<br>"
        else:
            output += f"Skipped brand: {obj.BRAND_NAME}<br>"

    for c in cars:
        brand = cars_brand.objects.get(BRAND_NAME=c["CAR_BRAND"])
        obj, created = cars_info.objects.get_or_create(
            CAR_NAME=c["CAR_NAME"],
            CAR_MODEL=c["CAR_MODEL"],
            CAR_PRICE=c["CAR_PRICE"],
            CAR_BRAND=brand
        )
        if created:
            output += f"Created car: {obj.CAR_NAME}<br>"
        else:
            output += f"Skipped car: {obj.CAR_NAME}<br>"

    return HttpResponse(output)

def cars_page(request):
    items = cars_info.objects.all()
    return render(request, "cars_template.html", {"items": items})
