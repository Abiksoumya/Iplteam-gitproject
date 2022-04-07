from django.shortcuts import render
from player.models import player

# Create your views here.
def myplayer(request):
    my_players=player.objects.order_by('-player_name')
    data={
        'my_players':my_players,
    }
    return render(request,'player/myplayer.html',data)
