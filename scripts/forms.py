from flask_wtf import Form
from wtforms import StringField, validators, TextAreaField, SelectField, SelectMultipleField
from wtforms.fields.html5 import DateField
from wtforms.widgets import ListWidget, CheckboxInput

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(html_tag='ul', prefix_label=True)
    option_widget = CheckboxInput()

class RequestForm(Form):
    title = StringField('Title:', validators=[validators.required(), validators.Length(min=1, max=50)])
    description = TextAreaField('Description:', validators=[validators.required(), validators.Length(min=1, max=500)])
    client = SelectField('Client:', choices=[('A', 'Client A'), ('B', 'Client B'), ('C', 'Client C')])
    date = DateField(id='datepick')
    area = MultiCheckboxField('Product Area:', choices=[('1', 'Policies'), ('2', 'Billings'), ('3', 'Claims'), ('4', 'Reports')])
