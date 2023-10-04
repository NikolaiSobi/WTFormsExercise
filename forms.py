from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class PetForm(FlaskForm):
    """Add Pets"""

    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Species name", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=100)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=1)])
    # available = BooleanField("Available to adopt", validators=[])