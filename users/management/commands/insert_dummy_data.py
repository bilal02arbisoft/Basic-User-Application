from datetime import datetime
from django.core.management.base import BaseCommand
from users.models import CustomUser, DateTimeModel
from faker import Faker
import pytz


class Command(BaseCommand):
    help = 'Insert dummy users and PST date times into the database'
    fake = Faker()

    def handle(self, *args, **kwargs):
        # self.insert_dummy_users()
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
        pst_timezone = pytz.timezone('America/Los_Angeles')
        for i in range(100):
            current_pst_time = datetime.now(pst_timezone)
            naive_pst_time = current_pst_time.replace(tzinfo=None)
            DateTimeModel.objects.create(datetime=naive_pst_time)
            self.stdout.write(self.style.SUCCESS(f'Successfully created PST datetime: {naive_pst_time}'))
        self.stdout.write(self.style.SUCCESS('Completed inserting dummy PST datetime'))
