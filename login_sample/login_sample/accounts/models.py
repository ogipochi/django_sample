from django.db import models

class MusicInstrument(models.Model):
    name = models.CharField(max_length = 100)

class MusicCareer(models.Model):
    musicInstrument = models.ForeignKey(MusicInstrument,on_delete=models.CASCADE)
    experiment = models.CharField(max_length = 50)


class MusicCareerList(models.Model):
    career = models.ForeignKey(MusicCareer,on_delete=models.CASCADE)

class UserInfo(models.Model):
    name = models.CharField(max_length = 100,null=False)
    musicCareerList = models.ManyToManyField(MusicCareerList)

    




