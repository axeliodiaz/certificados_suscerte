from django.db import models
from django.contrib.auth.models import AbstractUser


class Persona(AbstractUser):
    cedula = models.PositiveIntegerField(default=1, unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'persona'

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
