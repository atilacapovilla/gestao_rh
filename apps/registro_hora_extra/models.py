from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=50, help_text='Motivo da hora extra')

    def __str__(self):
        return self.motivo
