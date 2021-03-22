from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    user_visits = Visit.objects.filter(passcard=passcard, leaved_at__isnull=False)
    long_visits = []
    super_long_visits = []
    for user_visit in user_visits:
        if Visit.is_visit_long(user_visit, 50):
            long_visits.append(user_visit)
            continue
        if Visit.is_visit_long(user_visit, 1000):
            super_long_visits.append(user_visit)
            continue
    print(long_visits)
    print(super_long_visits)
    # Программируем здесь

    this_passcard_visits = [
        {
            "entered_at": "11-04-2018",
            "duration": "25:03",
            "is_strange": False
        },
    ]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
