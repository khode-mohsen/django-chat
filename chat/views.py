from django.shortcuts import render, HttpResponse, get_object_or_404
from chat.models import Room ,Message

def rooms(request):
    rooms = Room.objects.all()[:5]
    return render(request, 'chat/rooms.html', context = {'rooms':rooms})
def chatRoom(request, slug):
    room  = Room.objects.get(slug=slug)
    print(room)
    messages = Message.objects.filter(room=room)
    context = {'room':room , 'messages':messages}
    return render(request, 'chat/chatRoom.html', context = context)
