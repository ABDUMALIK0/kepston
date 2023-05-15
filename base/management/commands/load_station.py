import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from ...models import MapLocation

class Command(BaseCommand):
    help = 'Load data from csv'
    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR /'data'/ 'fire_archive_M6_156000.csv'
        keys = ('latitude', 'longitude','acq_date')
        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k:row[k] for k in keys})
        count = 10
        for record in records:
            MapLocation.objects.get_or_create(
                latitude = record['latitude'],
                longitude = record['longitude'],
                date = record['acq_date']
            )
            count += 1
            if count == 20:
                break