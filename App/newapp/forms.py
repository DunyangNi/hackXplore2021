from django import forms


class ChoiceForm(forms.Form):
    question1 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question2 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question3 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question4 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question5 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question6 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question7 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question8 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    question9 = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=[('1', 'Not at all'),
                                           ('2', 'Several days'),
                                           ('3', 'More than half the days'),
                                           ('4', 'Nearly every day')])
    journal = forms.CharField(widget=forms.Textarea())
