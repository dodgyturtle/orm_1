from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    user_visits = Visit.objects.filter(passcard=passcard, leaved_at__isnull=False)
    this_passcard_visits = []
    for user_visit in user_visits:
        strange_flag = Visit.is_visit_long(user_visit)
        visit_duration = user_visit.leaved_at - user_visit.entered_at
        this_passcard_visits.append(
            {
                "entered_at": user_visit.entered_at,
                "duration": format_duration(visit_duration),
                "is_strange": strange_flag,
            }
        )
    context = {"passcard": passcard, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
