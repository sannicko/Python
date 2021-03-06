import account.forms
from django import forms
from django.conf import settings
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _
from .models import ApplicationUser

from account.hooks import hookset
from account.forms import SignupForm
from django.forms import ModelForm
from employee.models import Employee

class userLoginForm(forms.Form):
    identifier_field = "email"
    email = forms.CharField(label=_("Email"), max_length=60)
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(render_value=False)
    )   

    def clean(self, *args, **kwargs):
        print '>>> In clean function of Form <<'
        cleaned_data = super(userLoginForm, self).clean(*args, **kwargs)
        if self._errors:
            return
        user = auth.authenticate(**self.user_credentials())
        if user:
            self.user = user
        else:
            raise forms.ValidationError(
                _("Please make sure you are providing valid Username and password."))
        return cleaned_data

    def user_credentials(self):
        self.identifier_field = "email"
        return hookset.get_user_credentials(self, self.identifier_field)

class EmployeeForm(ModelForm):
    # ceiling_mechanic = forms.BooleanField()
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'convicted_or_not': forms.RadioSelect,
            'allowed_in_usa':forms.RadioSelect

        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False 


class UserSignUpForm(forms.Form):

    # MIN_LENGTH = settings.PASSWORD_MIN_LENGTH
    MIN_LENGTH = 5
    email = forms.EmailField(label=_('email'), required=True, max_length=255)
    first_name = forms.CharField(max_length=30, label=_('First Name'))
    password = forms.CharField( widget=forms.PasswordInput(), label=_("Password"), min_length=6)

    class Meta:
        model = ApplicationUser
        fields = ('first_name', 'last_name','phoneNumber','password')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserSignUpForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < self.MIN_LENGTH:
            raise forms.ValidationError("The password must be at least %d characters long." % self.MIN_LENGTH)
        else:
            print '>>> password is :', password
        return password

