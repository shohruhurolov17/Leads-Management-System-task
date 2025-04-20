from django.db import models
from apps.leads.choices import LeadStatus


class Lead(models.Model):

    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)

    email = models.EmailField()

    resume = models.FileField(upload_to='resumes/')

    status = models.CharField(
        max_length=15,
        choices=LeadStatus,
        default=LeadStatus.PENDING
    )

    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:

        db_table = 'leads'
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-created_time']
