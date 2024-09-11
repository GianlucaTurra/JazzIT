from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel

from utils import abstract_models 

class Suggestion(abstract_models.Model, TimeStampedModel):

    user = models.ForeignKey(User, verbose_name=_("Created by"), on_delete=models.CASCADE)
    base_music = models.CharField(_("If you liked"), max_length=50, null=False, blank=False)
    suggested_music = models.CharField(_("You'll like"), max_length=50, null=False, blank=False)
    description = models.TextField(_("Additional description"))

    class Meta:
        verbose_name = _("Music suggestion")
        verbose_name_plural = _("Music suggestions")

    def __str__(self):
        return f'If you liked {self.base_music} you\'ll like {self.suggested_music}'

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
