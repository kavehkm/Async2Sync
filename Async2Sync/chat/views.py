# dj
from django.views import View
from django.shortcuts import render


ROOMS = [
    'lobby',
    'chatroom1',
    'chatroom2'
]


class IndexView(View):
    """Index View"""
    def get(self, request):
        return render(request, 'chat/index.html', {'rooms': ROOMS})


class RoomView(View):
    """Room View"""
    def get(self, request, room_name):
        return render(request, 'chat/room.html', {'room_name': room_name})
