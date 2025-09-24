from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from faker import Faker
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings, and reviews."

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear old data (optional, comment out if you want to keep existing)
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

        self.stdout.write(self.style.WARNING("Old data deleted."))

        # Create sample listings
        listings = []
        for _ in range(10):  # Create 10 listings
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                price=round(random.uniform(100, 10000), 2),
            )
            listings.append(listing)

        self.stdout.write(self.style.SUCCESS("10 Listings created."))

        # Create sample bookings
        for listing in listings:
            for _ in range(random.randint(1, 3)):  # 1–3 bookings per listing
                Booking.objects.create(
                    listing=listing,
                    user_name=fake.name(),
                    user_email=fake.email(),
                )

        self.stdout.write(self.style.SUCCESS("Sample Bookings created."))

        # Create sample reviews
        for listing in listings:
            for _ in range(random.randint(1, 5)):  # 1–5 reviews per listing
                Review.objects.create(
                    listing=listing,
                    user_name=fake.name(),
                    rating=random.randint(1, 5),
                    comment=fake.sentence(nb_words=12),
                )

        self.stdout.write(self.style.SUCCESS("Sample Reviews created."))

        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))
