from django import forms


class textForm(forms.Form):
    searchText = forms.CharField(max_length=100)
