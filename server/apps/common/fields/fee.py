from typing import Final

from django.conf import settings
from django.db.models import CharField, DecimalField
from django.utils.translation import ugettext_lazy as _

from ._multicolumn import MultiColumnField


class FlatChoicesMixin:
    @classmethod
    def flat_choices(cls) -> tuple:
        try:
            return tuple(full_choice[0] for full_choice in cls.CHOICES)
        except AttributeError:
            raise AttributeError('Inheriting child must have class attribute CHOICES')
        except IndexError:
            raise IndexError('CHOICES must contain tuples - (raw_value, description)')


class FeeType(FlatChoicesMixin):
    FIXED: Final[str] = 'fixed'
    PERCENTAGE: Final[str] = 'percentage'

    CHOICES: Final[tuple] = (
        (FIXED, _("Fixed")),
        (PERCENTAGE, _("Percentage")),
    )


class FeeField(MultiColumnField):
    def __init__(self, *args, **kwargs):
        self.fields = {
            'type': CharField(
                max_length=14,
                choices=FeeType.CHOICES,
                verbose_name=_("Type"),
            ),
            'value': DecimalField(
                max_digits=10,
                decimal_places=settings.MONEY_DECIMAL_PLACES,
                verbose_name=_("Value"),
            )
        }
        super(FeeField, self).__init__(*args, **kwargs)
