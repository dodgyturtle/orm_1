import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit

def print_passcards_from_db():
    passcards = Passcard.objects.all()
    for passcard in passcards:
        print("owner_name:", passcard.owner_name,"\n",
        "passcode:", passcard.passcode,"\n",
        "created_at:", passcard.created_at,"\n",
        "is_active", passcard.is_active)
        

if __name__ == "__main__":
    # Программируем здесь
    print_passcards_from_db()