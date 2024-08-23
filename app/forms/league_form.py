from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, URL

class LeagueForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    draft_type = SelectField('Choose an option', choices=[('Snake', 'Snake'), ('Auction', 'Auction')], validators=[DataRequired()])
    scoring_system = SelectField('Choose an Option', choices=[('Standard', 'Standard'), ('Points Per Reception (PPR)', 'Points Per Reception (PPR)'), ('Half PPR', 'Half PPR')], validators=[DataRequired()])
    max_teams = SelectField('Choose an Option', choices=[('8', '8'), ('10', '10'), ('12', '12'), ('14', '14')], validators=[DataRequired()])
    submit = SubmitField('Submit')
