from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, 5)
    try:
        rooms = paginator.page(int(page))
    except Exception:
        rooms = paginator.page(1)
    return render(request, "rooms/home.html", {"page": rooms})
