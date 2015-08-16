__author__ = 'dave'

from django import forms
from crispy_forms.helper import FormHelper
from allauth.account.forms import LoginForm


# Reusable crispy forms for the website
# TODO implement the extended login form at a later time

class ExtendedLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.username = forms.CharField(label="Username", required=True)
        super.__init__()
