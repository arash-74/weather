from django import forms


class InputForm(forms.Form):
    city_input = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Please enter city name'}))

    def clean_city_input(self):
        city_input = self.cleaned_data['city_input']
        if not city_input.isalpha():
            raise forms.ValidationError('Please enter city name correctly')
        return city_input
