from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class LeagueForm(FlaskForm):
    name = StringField('League Name', validators=[DataRequired()])

    draft_type = SelectField('Draft Type',
                             choices=[('Snake', 'Snake'), ('Auction', 'Auction')],
                             validators=[DataRequired()])

    scoring_system = SelectField('Scoring System',
                                 choices=[('Standard', 'Standard'),
                                          ('PPR', 'Points Per Reception (PPR)'),
                                          ('Half-PPR', 'Half-PPR')],
                                 validators=[DataRequired()])

    max_teams = SelectField('Max Teams',
                            choices=[('8', '8'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16')],
                            validators=[DataRequired()])

    image_url = StringField('Image URL')

    submit = SubmitField('Submit')
