from django.db import models

# Create your models here.

class player(models.Model):
    player_name=models.CharField(max_length=225)
    player_photo=models.ImageField(upload_to='photos/%Y/%M/%D/')
    team_names=models.CharField(max_length=100)
    player_price=models.IntegerField()
    playing_ststus=models.CharField(max_length=100)
    player_role=models.CharField(max_length=100)


    def __str__(self):
        return self.player_name
