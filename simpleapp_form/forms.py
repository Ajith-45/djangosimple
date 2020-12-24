from django.forms import ModelForm
from .models import Userform

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class Usermodelform(ModelForm):
    class Meta:
        model = Userform
        fields = ['first_name','last_name','email','regno','clg','city','state','zipcode']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Submit'))
