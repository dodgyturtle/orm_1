from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def format_duration(duration):
    seconds = duration.total_seconds()
    hour = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    if duration.days != 0:
        return f"{ duration.days } дней { hour } ч. { minutes } м."
    return f"{ hour } ч. { minutes } м."


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    all_visitors = Visit.objects.filter(leaved_at__isnull=True)
    for visitor in all_visitors:
        user_entered = localtime(visitor.entered_at)
        user_in_warehouse_passcard = visitor.passcard
        duration = Visit.get_duration(visitor)
        non_closed_visits.append(
            {
                "who_entered": user_in_warehouse_passcard.owner_name,
                "entered_at": user_entered,
                "duration": format_duration(duration),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    print(context)
    return render(request, "storage_information.html", context)
