from django.db import models

# Create your models here.
class MyTeams(models.Model):
    team_name=models.CharField(max_length=100)
    team_icon=models.ImageField(upload_to='photos/%Y/%M/%D/')
    players_count=models.IntegerField()
    top_batsman=models.CharField(max_length=225)
    top_batsman=models.CharField(max_length=225)
    top_batsman=models.CharField(max_length=225)
    top_bolower=models.CharField(max_length=225)
    top_bolower=models.CharField(max_length=225)
    top_bolower=models.CharField(max_length=225)
    top_bolower=models.CharField(max_length=225)
    championship_won=models.IntegerField()


    def __str__(self):
        return self.team_name
    


