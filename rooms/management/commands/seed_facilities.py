from django.core.management.base import BaseCommand
from rooms import models as room_models

NAME = "facilities"


class Command(BaseCommand):

    help = f"This Commands creates {NAME}"

    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="how many {NAME} do you want to create",
        )
    """

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:
            room_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} {NAME} created!"))
