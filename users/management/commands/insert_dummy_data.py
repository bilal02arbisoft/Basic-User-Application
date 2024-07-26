from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from users.models import CustomUser, DateTimeModel
from faker import Faker
import pytz


class Command(BaseCommand):
    help = 'Insert dummy users and PST date times into the database'
    fake = Faker()

    def handle(self, *args, **kwargs):

        self.insert_dummy_users()
        self.insert_dummy_pst_datetime()

    def insert_dummy_users(self):
        for i in range(100):
            email = self.fake.email()
            first_name = f'First{i}'
            last_name = f'Last{i}'
            password = 'password123'
            CustomUser.objects.create_user(email=email, first_name=first_name,
                                           last_name=last_name, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {email}'))

    def insert_dummy_pst_datetime(self):
        for i in range(100):
            pst_timezone = pytz.timezone('America/Los_Angeles')
            current_pst_time = datetime.now(pst_timezone)
            DateTimeModel.objects.create(datetime=current_pst_time)
            self.stdout.write(self.style.SUCCESS(f'Successfully created PST datetime: {current_pst_time}'))
        self.stdout.write(self.style.SUCCESS('Completed inserting dummy PST datetime'))
