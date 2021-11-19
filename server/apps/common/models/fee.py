from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..fields.fee import FeeField


class Fee(models.Model):
    name = models.CharField(
        max_length=254,
        verbose_name=_("Name"),
    )
    fee = FeeField(verbose_name=_("Fee"))

    objects = models.Manager()

    class Meta:
        verbose_name = 'fee'
        verbose_name_plural = 'fees'

    def __str__(self) -> str:
        return self.name
