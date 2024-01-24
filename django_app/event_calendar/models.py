from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class CalendarEvent(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    date_created = models.DateField(default=datetime.now)
    event_start_date = models.DateTimeField(default=datetime.now)
    event_end_date = models.DateTimeField(default=datetime.now)
    colors = [
        ('bg-primary', 'Primary'),
        ('bg-secondary', 'Secondary'),
        ('bg-success', 'Success'),
        ('bg-info', 'Info'),
        ('bg-warning', 'Warning'),
        ('bg-danger', 'Danger'),
        ('bg-light', 'Light'),
        ('bg-dark', 'Dark'),
        ('bg-white', 'White'),
        ('bg-transparent', 'Transparent'),
        ('bg-gradient-primary', 'Gradient Primary'),
        ('bg-gradient-secondary', 'Gradient Secondary'),
        ('bg-gradient-success', 'Gradient Success'),
        ('bg-gradient-info', 'Gradient Info'),
        ('bg-gradient-warning', 'Gradient Warning'),
        ('bg-gradient-danger', 'Gradient Danger'),
        ('bg-gradient-light', 'Gradient Light'),
        ('bg-gradient-dark', 'Gradient Dark'),
        ('bg-gradient-faded-primary', 'Faded Gradient Primary'),
        ('bg-gradient-faded-secondary', 'Faded Gradient Secondary'),
        ('bg-gradient-faded-success', 'Faded Gradient Success'),
        ('bg-gradient-faded-info', 'Faded Gradient Info'),
        ('bg-gradient-faded-warning', 'Faded Gradient Warning'),
        ('bg-gradient-faded-danger', 'Faded Gradient Danger'),
        ('bg-gradient-faded-light', 'Faded Gradient Light'),
        ('bg-gradient-faded-dark', 'Faded Gradient Dark'),
        ('bg-gradient-faded-white', 'Faded Gradient White'),
        ('bg-gradient-faded-primary-vertical', 'Faded Primary Vertical'),
        ('bg-gradient-faded-secondary-vertical', 'Faded Secondary Vertical'),
        ('bg-gradient-faded-success-vertical', 'Faded Success Vertical'),
        ('bg-gradient-faded-info-vertical', 'Faded Info Vertical'),
        ('bg-gradient-faded-warning-vertical', 'Faded Warning Vertical'),
        ('bg-gradient-faded-danger-vertical', 'Faded Danger Vertical'),
        ('bg-gradient-faded-light-vertical', 'Faded Light Vertical'),
        ('bg-gradient-faded-dark-vertical', 'Faded Dark Vertical'),
        ('bg-gradient-faded-white-vertical', 'Faded White Vertical'),
    ]
    color = models.CharField(max_length=40, choices=colors, default='bg-primary')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.author.username} on {self.date_created}'