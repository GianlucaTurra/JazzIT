from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel

from utils import abstract_models 


class AdviceCategory(models.TextChoices):
    ARTIST = 'AR', _('Artist')
    ALBUM = 'AL', _('Album')
    TRACK = 'TR', _('Track')


class MusicAdvice(abstract_models.Model, TimeStampedModel):

    user = models.ForeignKey(User, verbose_name=_("Created by"), on_delete=models.CASCADE)
    base = models.CharField(_("If you liked"), max_length=100, null=False, blank=False)
    advice = models.CharField(_("You'll like"), max_length=100, null=False, blank=False)
    description = models.TextField(_("Additional description"))
    category = models.CharField(_("Advice category"), max_length=10, choices=AdviceCategory, default=AdviceCategory.TRACK)

    class Meta:
        verbose_name = _("Music advice")
        verbose_name_plural = _("Music advices")

    def __str__(self):
        return f'If you liked {self.base} you\'ll like {self.advice}'

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    