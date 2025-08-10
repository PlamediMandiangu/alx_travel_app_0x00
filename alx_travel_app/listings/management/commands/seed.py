from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        listings_data = [
            {"title": "Cozy Apartment", "description": "A cozy apartment in the city center", "price_per_night": 75.00, "location": "Cape Town"},
            {"title": "Beach House", "description": "Beautiful beach house with ocean view", "price_per_night": 150.00, "location": "Durban"},
            {"title": "Mountain Cabin", "description": "Rustic cabin in the mountains", "price_per_night": 90.00, "location": "Drakensberg"}
        ]

        for data in listings_data:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Sample listings created successfully."))
