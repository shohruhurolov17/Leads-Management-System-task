from django.db.models import TextChoices


class LeadStatus(TextChoices):

    PENDING = 'pending'
    REACHED_OUT = 'reached_out'