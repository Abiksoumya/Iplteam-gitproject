from django.contrib import admin
from matplotlib.image import thumbnail
from .models import MyTeams

# Register your models here.
class MyTeamsAdmin(admin.ModelAdmin):
    
    list_display =('team_name','players_count','championship_won') 
    list_display_links=('team_name','players_count')
    search_fields=('team_name','championship_won','top_batsman','top_bolower')

admin.site.register(MyTeams,MyTeamsAdmin)


