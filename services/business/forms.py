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
    company_website = forms.URLField(max_length=200, initial='https://')
    business_category = forms.CharField()
    address = forms.CharField(max_length=100)
    business_description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'rows':'10', 'cols':'40'}))
    Photo = forms.ImageField()

class businessLogin(forms.Form):
    Email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)