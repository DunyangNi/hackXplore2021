from django import forms

CHOICES = [('1', '1'),
           ('2', '2'),
           ('3', '3')]


class answerForm(forms.Form):
    value1 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
