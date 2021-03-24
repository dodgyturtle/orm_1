from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def format_duration(duration):
    seconds = duration.total_seconds()
    days = int(seconds // 3600 // 24)
    hours = int(seconds // 3600 % 24)
    minutes = int((seconds % 3600) // 60)
    if days != 0:
        return f"{ days } д. { hours } ч. { minutes } м."
    return f"{ hours } ч. { minutes } м."


def storage_information_view(request):
    non_closed_visits = []
    visitors = Visit.objects.filter(leaved_at__isnull=True)
    for visitor in visitors:
        user_entered = localtime(visitor.entered_at)
        user_in_warehouse_passcard = visitor.passcard
        duration = visitor.get_duration()
        non_closed_visits.append(
            {
                "who_entered": user_in_warehouse_passcard.owner_name,
                "entered_at": user_entered,
                "duration": format_duration(duration),
                "is_strange": visitor.is_visit_long(),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
