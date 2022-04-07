
from django.shortcuts import render
from MyTeams.models import MyTeams

# Create your views here.
def iplteam(request):
    teams=MyTeams.objects.order_by('-team_name')
    data={
        'teams':teams,
    }

    return render(request,'myteams/myteams.html',data)