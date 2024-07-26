from django.core.management.base import BaseCommand
import pytz
from users.models import DateTimeModel


class Command(BaseCommand):
    help = 'Convert dates between PST and UTC in batches of 10'

    def handle(self, *args, **kwargs):
        pst = pytz.timezone('America/Los_Angeles')
        utc = pytz.UTC
        batch_size = 10
        latest_record = DateTimeModel.objects.order_by('-count').first()
        current_count = latest_record.count if latest_record else 0
        to_utc = (current_count // 100) % 2 == 0
        if to_utc:

            records = DateTimeModel.objects.filter(is_utc=False).order_by('count')[:batch_size]
        else:
            records = DateTimeModel.objects.filter(is_utc=True).order_by('count')[:batch_size]

        if not records.exists():

            self.stdout.write(self.style.SUCCESS('No records to convert'))

            return

        for record in records:
            if to_utc:

                if record.datetime.tzinfo is None:

                    localized_dt = pst.localize(record.datetime)
                else:
                    localized_dt = record.datetime
                record.datetime = localized_dt.astimezone(utc).replace(tzinfo=None)
                record.is_utc = True
            else:
                if record.datetime.tzinfo is None:

                    localized_dt = utc.localize(record.datetime)
                else:
                    localized_dt = record.datetime
                record.datetime = localized_dt.astimezone(pst).replace(tzinfo=None)
                record.is_utc = False
            record.count = current_count + 1
            record.save()
            current_count += 1
        self.stdout.write(self.style.SUCCESS(f'Converted {len(records)} records'))


