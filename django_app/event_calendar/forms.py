from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django import forms
from .models import CalendarEvent

class CalendarEventBodyForm(forms.ModelForm):
    foo = forms.CharField(widget=SummernoteWidget())
    content = forms.CharField(widget=SummernoteInplaceWidget())

    class Meta:
        model = CalendarEvent
        fields = ('body',)
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['title', 'event_start_date', 'event_end_date', 'color', 'approved']
        widgets = {
            'event_start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'event_end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(CalendarEventForm, self).__init__(*args, **kwargs)
        self.fields['event_start_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['event_end_date'].input_formats = ('%Y-%m-%dT%H:%M',)