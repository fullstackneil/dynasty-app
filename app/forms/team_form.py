from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from ..models import League

class TeamForm(FlaskForm):
    name = StringField('Please create a team name',
                       validators=[DataRequired(), Length(max=50)])

    league_id = SelectField('Please select a league',
                            coerce=int,
                            validators=[DataRequired()])

    submit = SubmitField('Create Team')

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)

        # Populate league choices
        self.league_id.choices = [(league.id, league.name) for league in League.query.all()]
