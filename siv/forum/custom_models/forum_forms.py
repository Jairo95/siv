from django import forms
from forum.models import WorryMessage


class WorryMessageForm(forms.ModelForm):

    class Meta:
        model = WorryMessage
        fields = ['worry_message', 'worry_category', 'worry_type']

    def __init__(self, *args, **kwargs):
        super(WorryMessageForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == 'worry_message':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })