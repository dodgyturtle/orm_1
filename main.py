import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()
from datacenter.models import Passcard, Visit

def print_passcards_from_db():
    passcard_db = Passcard.objects.all()
    print('Количество пропусков:', Passcard.objects.count())
    passcards = [ passcard.owner_name for passcard in passcard_db if passcard.is_active ]
    print("Активных пропусков:", len(passcards))
        

if __name__ == "__main__":
    # Программируем здесь
    print_passcards_from_db()