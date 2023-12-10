import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            rows = list(csv.DictReader(file, delimiter=';'))

        for row in rows:
            try:
                phone = Phone.objects.get(pk=row['id'])
            except Phone.DoesNotExist:
                phone = Phone(pk=row['id'])
            phone.name = row['name']
            phone.price = row['price']
            phone.image = row['image']
            phone.release_date = row['release_date']
            phone.lte_exists = row['lte_exists'].lower() == 'true'
            phone.slug = slugify(row['name'])
            phone.save()
            print(f'created {phone}')
