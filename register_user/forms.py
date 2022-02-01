from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UsernameField
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIP-Client"),
    (CLIENT, "CLIENT")
)
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER"),
)
LAPTOP = 1
PC = 2
ANDROID = 3
IOS = 4
DEVICE_TYPE = (
    (LAPTOP,'LAPTOP'),
    (PC,'PC'),
    (ANDROID,'ANDROID'),
    (IOS,'IOS'),
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    device = forms.ChoiceField(choices=DEVICE_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'local',
            'phone_number',
            'device',
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Email','id':'ziga'}
    ))
    username = UsernameField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'username','id':'hello'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Password','id':'hi'}
    ))