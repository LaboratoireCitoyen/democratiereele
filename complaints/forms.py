from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import (
    Layout, Fieldset, HTML, Row, Column, Panel,
    ButtonHolder, ButtonHolderPanel, ButtonGroup, Button, Submit,
    InlineField, InlineJustifiedField,
    SwitchField, InlineSwitchField
)

import autocomplete_light

from .models import Complaint, Action


class ComplaintForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Row(
                Fieldset(
                    _('Complaint'),
                    Row('name'),
                    Row('description'),
                    Row('photo'),
                    Row('city'),
                    Row('tags'),
                    Row(Submit('submit', _('Submit'),
                        css_class='success'),
                    ),
                    css_class='login-required',
                )
            ),
        )

        self.base_fields['tags'].required = False
        super(ComplaintForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ('city', 'photo', 'tags', 'name', 'description')
        model = Complaint


class ActionForm(autocomplete_light.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action = kwargs.pop('form_action', '.')
        self.helper.layout = Layout(
            Row(
                Fieldset(
                    _('Propose an action'),
                    Row('name'),
                    Row('description'),
                    Row('complaint'),
                    Row(Submit('submit', _('Submit'),
                        css_class='success'),
                    ),
                    css_class='login-required',
                )
            ),
        )

        super(ActionForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = ('name', 'description', 'complaint')
        model = Action
