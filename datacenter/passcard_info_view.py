from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    user_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for user_visit in user_visits:
        visit_duration = user_visit.get_duration()
        this_passcard_visits.append(
            {
                "entered_at": user_visit.entered_at,
                "duration": format_duration(visit_duration),
                "is_strange": user_visit.is_visit_long(),
            }
        )
    context = {"passcard": passcard, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
