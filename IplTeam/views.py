from django.shortcuts import render
from .models import Team
from MyTeams.models import MyTeams
from player.models import player


# Create your views here.
def home(request):
    teams=Team.objects.all()
    ipl_teams=MyTeams.objects.order_by('-team_name')
    all_teams=MyTeams.objects.order_by('-team_name')
    my_players=player.objects.order_by('-player_name')
    
    data={
        'teams': teams,
        'ipl_teams': ipl_teams,
        'all_teams': all_teams,
        'my_players':my_players,
        
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams': teams
    }
    return render(request,'pages/about.html',data)

def contact(request):
    return render(request,'pages/contact.html')    