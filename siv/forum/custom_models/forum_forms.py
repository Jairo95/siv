from django import forms
from forum.models import WorryMessage, OpinionMessage


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


class OpinionMessageForm(forms.ModelForm):

    class Meta:
        model = OpinionMessage
        fields = ['opinion_message']

    def __init__(self, *args, **kwargs):
        super(OpinionMessageForm, self).__init__(*args, **kwargs)
        self.fields['opinion_message'].widget.attrs.update({'class': 'form-control'})


