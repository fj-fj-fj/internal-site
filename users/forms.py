""" This module contains forms for registration of 
        two types of user `employee` and `boss`. 
    
    It also contains crispy (CrispyUserCreationForm):
    https://django-crispy-forms.readthedocs.io/en/latest/

"""
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import User, Boss, Employee

        
class CrispyUserCreationForm(UserCreationForm):
    """General model and fields form both types of user"""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        """Crispy: set up some basic `FormHelper` attributes"""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class BossSignUpForm(CrispyUserCreationForm):
    pass


class EmployeeSignUpForm(CrispyUserCreationForm):
    pass


class BaseEmployeeLevelForm(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False
            form.fields['level'].required = False
            form.fields['level'].label = 'Ваш уровень опыта'


EmployeeLevelForm = inlineformset_factory(
    User, Employee, 
    fields=('level',),
    can_delete=False, 
    formset=BaseEmployeeLevelForm
)
