from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('FILM','FILM'),
        ('SERIAL','SERIAL')
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        model = models.Film
        fields = [
            'media_type',
            'create_date',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'FILM':
            film_parser = parser.parser()
            for i in film_parser:
                models.Film.objects.create(**i)
        elif self.data['media_type'] == 'SERIAL':
            serial_parser = parser.parser()
            for i in serial_parser:
                models.Film.objects.create(**i)