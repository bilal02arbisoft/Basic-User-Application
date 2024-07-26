from django.core.management.base import BaseCommand
from users.models import DateTimeModel, ConversionState
import pytz


class Command(BaseCommand):
    help = 'Convert dates between PST and UTC in batches of 10'

    def to_pst_exists(self):
        records = DateTimeModel.objects.filter(is_utc=True)[:10]
        return records.exists()

    def to_utc_exists(self):

        records = DateTimeModel.objects.filter(is_utc=False)[:10]

        return records.exists()

    def get_records_to_utc(self):

        return DateTimeModel.objects.filter(is_utc=False)[:10]

    def get_records_to_pst(self):

        return DateTimeModel.objects.filter(is_utc=True)[:10]

    def handle(self, *args, **kwargs):
        pst = pytz.timezone('America/Los_Angeles')
        utc = pytz.UTC
        conversion_state, created = ConversionState.objects.get_or_create(id=1)
        if conversion_state.to_utc:

            records_to_utc = self.get_records_to_utc()
            for record in records_to_utc:
                if record.datetime.tzinfo is None:

                    localized_dt = pst.localize(record.datetime)
                else:
                    localized_dt = record.datetim
                record.datetime = localized_dt.astimezone(utc).replace(tzinfo=None)
                record.is_utc = True
                record.save()
            self.stdout.write(self.style.SUCCESS(f'Converted {records_to_utc.count()} records to UTC'))
            if not self.to_utc_exists():

                conversion_state.to_utc = False
                conversion_state.save()
        else:
            records_to_pst = self.get_records_to_pst()
            for record in records_to_pst:
                if record.datetime.tzinfo is None:

                    localized_dt = utc.localize(record.datetime)
                else:
                    localized_dt = record.datetime
                record.datetime = localized_dt.astimezone(pst).replace(tzinfo=None)
                record.is_utc = False
                record.save()
            self.stdout.write(self.style.SUCCESS(f'Converted {records_to_pst.count()} records to PST'))
            if not self.to_pst_exists():

                conversion_state.to_utc = True
                conversion_state.save()




