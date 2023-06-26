from django.db import models

# Create your models here.


class jadwalModels(models.Model):
    Tanggal = models.CharField(max_length=50)
    Imsyak  = models.TimeField()
    Subuh   = models.TimeField()
    Terbit  = models.TimeField()
    Dhuha  = models.TimeField()
    Dzuhur  = models.TimeField()
    Asar    = models.TimeField()
    Magrib  = models.TimeField()
    Isya    = models.TimeField()

    def _str_(self):
        return self.Tanggal