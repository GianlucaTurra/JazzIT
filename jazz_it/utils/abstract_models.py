import uuid
from django.db import models


class Model(models.Model):
    """Utility class for uuid
    This only inherit the django Model class to chango the
    default id with the uuid
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        """
        Defines the model as an abstract class
        """
        abstract = True
