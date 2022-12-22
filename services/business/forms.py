from django import forms

class businessPersonRegistration(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    mobile_number = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class businessRegistration(forms.Form):
    company_name = forms.CharField(max_length=100)
    business_category = forms.CharField()
    address = forms.CharField(max_length=100)
    business_description = forms.CharField(max_length=300)
    Photo = forms.ImageField()

class businessLogin(forms.Form):
    Email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)