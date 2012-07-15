from django.db import models
from model_utils import Choices

class Preference(models.Model):

    CHOICES = Choices(
            (0, 'inherited', 'Inherited'),
            (1, 'enabled', 'Enabled'),
            (2, 'disabled', 'Disabled'),
    )
    track_request = models.IntegerField(choices=CHOICES, default=CHOICES.inherited)

    # By enabling this, user will also get some error report (if exist) through web interface
    track_response = models.IntegerField(choices=CHOICES, default=CHOICES.inherited)

    email_errors = models.IntegerField(choices=CHOICES, default=CHOICES.inherited)
    signature = models.IntegerField(choices=CHOICES, default=CHOICES.inherited)
    signature_text = models.TextField(blank=True, null=True)
