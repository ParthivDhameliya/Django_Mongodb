from django import forms

class userRegistration(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)
    mobile_number = forms.IntegerField(required=False)
    city = forms.CharField()
    country = forms.CharField()
    zipcode = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class userLogin(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
