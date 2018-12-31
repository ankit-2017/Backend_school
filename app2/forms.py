from django import forms
from .models import *
from django.contrib.auth.models import User


class register(forms.ModelForm):

    username = forms.EmailField(widget=forms.EmailInput( attrs={ 'class':'form-control',
                                                            'placeholder': 'Enter Email Id' } ),
                                                            required=True, max_length=100 )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Enter your name'}),
                                 required=True, max_length=20)


    password = forms.CharField(
        widget=forms.PasswordInput( attrs={ 'class': 'form-control', 'placeholder': 'Enter Password' } ),
        required=True, max_length=100 )


    confirm_password = forms.CharField( widget=forms.PasswordInput(
        attrs={ 'class': 'form-control', 'placeholder': 'Confirm password' }
    ), required=True, max_length=100 )

    class Meta():
        model = User
        fields = ['username','first_name','password', 'confirm_password']


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            obj = User.objects.get(username=username)
        except:
            return self.cleaned_data['username']

        raise forms.ValidationError('Email Id already registered')

    def clean_confirm_password(self):
        pas = self.cleaned_data[ 'password' ]
        cpas = self.cleaned_data[ 'confirm_password' ]
        MIN_LENGTH = 8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError( "password and confirm password not matched" )
            else:
                if len( pas ) < MIN_LENGTH:
                    raise forms.ValidationError( "Password should have atleast %d characters" % MIN_LENGTH )
                if pas.isdigit( ):
                    raise forms.ValidationError( "Password should not all numeric" )
