from django import forms

class SummonerNameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    #message = forms.CharField(widget=forms.Textarea)