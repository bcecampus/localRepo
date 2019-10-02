from django import forms

class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First name'
            }
        )
    )

    last_name = forms.CharField(
        label="Enter Your last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'last name'
            }
        )
    )

    roll_no = forms.IntegerField(
        label="Enter Your Roll No",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Roll Number E.g. 15543'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )

    username = forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }
        )
    )

    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        )
    )




class Login(forms.Form):
    username = forms.CharField(
        label="Enter Your username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }
        )
    )

    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        )
    )