import django.forms
from django.forms import Form


class DummyForm(Form):
    feedback = django.forms.CharField(label='Feedback', min_length=5, max_length=100)
    rate = django.forms.IntegerField(label='Rating', min_value=0, max_value=100)
    file = django.forms.FileField(label='Photo', required=False)

    def clean_text(self):
        if 'abc' not in self.cleaned_data['feedback']:
            raise django.forms.ValidationError('Wrong subject of feedback')