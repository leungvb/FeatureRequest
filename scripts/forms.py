from flask_wtf import Form
from wtforms import StringField, validators, TextAreaField, SelectField, SelectMultipleField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.widgets import ListWidget, CheckboxInput

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(html_tag='ul', prefix_label=True)
    option_widget = CheckboxInput()

class RequestForm(Form):
    title = StringField('Title:', validators=[validators.required(), validators.Length(min=1, max=50, message='Invalid Length')])
    description = TextAreaField('Description:', validators=[validators.required(), validators.Length(min=1, max=500), validators.DataRequired('Must Provide A Description')])
    client = SelectField('Client:', choices=[('A', 'Client A'), ('B', 'Client B'), ('C', 'Client C')], validators= [validators.DataRequired('Pick a Client')])
    priority = SelectField('Priority:', choices=[(str(x),y) for x,y in enumerate(range(10))])
    date = DateField(id='datepick', validators= [validators.DataRequired('Pick a due date')])
    area = MultiCheckboxField('Product Area:', choices=[('Policies', 'Policies'), ('Billings', 'Billings'), ('Claims', 'Claims'), ('Reports', 'Reports')])
