from django import forms

class GraphForm(forms.Form):
    days = forms.IntegerField(
        label="Enter the number of days for the time window: This value will compare revisions from the event date + the value you enter",
        widget=forms.NumberInput(attrs={'class': 'form-field'}),
        min_value=1,
        max_value=500,
        initial=15,
        error_messages={
            'min_value': 'Please enter a value greater than or equal to 1.',
            'max_value': 'Please enter a value less than or equal to 500.'
        }
    )
