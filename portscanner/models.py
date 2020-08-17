from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Scan(models.Model):
    domain = models.CharField(_("Domain/IP"), max_length=50)
    scanner_ip = models.CharField(_("Scanner IP"), max_length=50)

    def __str__(self):
        return domain+'::'+scanner_ip