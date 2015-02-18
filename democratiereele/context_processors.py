from crispy_forms.helper import FormHelper


def no_form_tag(request):
    helper = FormHelper()
    helper.form_tag = False
    return {'no_form_tag': helper}
