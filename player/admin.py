from django.contrib import admin


from .models import player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display =('player_name','team_names','player_price','player_role','playing_ststus')
    list_display_links =('player_name','team_names')
    search_fields=('player_name','team_names','player_price','player_role')

admin.site.register(player,PlayerAdmin)