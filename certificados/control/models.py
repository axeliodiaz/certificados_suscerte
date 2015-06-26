from django.db import models

from personas.models import Persona
from certificados import settings 


class Certificado(models.Model):
    persona = models.ForeignKey(settings.AUTH_USER_MODEL)
    desde = models.DateField()
    hasta = models.DateField()
    revocacion = models.CharField(max_length=15)

    class Meta:
        db_table = 'certificado'

    def __unicode__(self):
        return u'%s' % (self.persona)
