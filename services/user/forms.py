from django import forms
import re

class userRegistration(forms.Form):
    first_name = forms.CharField(
        max_length=20, 
        error_messages={'required':'First name is required'},
        strip=True)
    last_name = forms.CharField(
        max_length=20, 
        error_messages={'required':'Last name is required'},
        strip=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder':'parthiv@gmail.com'}), 
        error_messages={'required':'Email is required'})
    mobile_number = forms.CharField(required=False, strip=True, max_length=10)
    city = forms.CharField(error_messages={'required':'City name is required'}, strip=True)
    country = forms.CharField(error_messages={'required':'Country name is required'}, strip=True)
    zipcode = forms.CharField(error_messages={'required':'Zipcode is required'}, strip=True)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Password is required'})
    agree = forms.BooleanField(error_messages={'required':'You must agree to contiue'}, label='I agree')

    def clean_password(self):
        fname = self.cleaned_data['first_name']
        lname = self.cleaned_data['last_name']
        password = self.cleaned_data['password']
        if bool(re.search('^[a-zA-Z0-9]*$', password)) == True:
            raise forms.ValidationError('Password should contain atleast one special character')
        if len(password) < 8:
            raise forms.ValidationError('Password should be atleast 8 characters long')
        if password.__contains__(fname) or password.__contains__(lname):
            raise forms.ValidationError('Password should not contain first or last name')

    def clean_mobile_number(self):
        mn = self.cleaned_data['mobile_number']
        if 0 < len(mn) < 10:
            raise forms.ValidationError("Mobile number should be 10 numbers long")
        for i in mn:
            if not i.isdigit():
                raise forms.ValidationError("Mobile number should only contain numbers")
        return mn


class userLogin(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
