import random
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
from ..models import League, Team, User

class TeamForm(FlaskForm):
    name = StringField('Please create a team name',
                       validators=[DataRequired(), Length(max=50)])

    league_id = SelectField('Please select a league',
                            coerce=int,
                            validators=[DataRequired()])

    # user_id = SelectField('Please confirm your Username',
    #                       coerce=int,
    #                       validators=[DataRequired()])

    draft_position = IntegerField('Draft Position',
                                  validators=[NumberRange(min=1, message="Draft position must be greater than 0")])

    submit = SubmitField('Create Team')

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)

        # Populate league choices
        self.league_id.choices = [(league.id, league.name) for league in League.query.all()]

        # Populate user choices
        # self.user_id.choices = [(user.id, user.username) for user in User.query.all()]

        # Get the league_id from the form data or default to the first league
        selected_league_id = self.league_id.data or (self.league_id.choices[0][0] if self.league_id.choices else None)

        if selected_league_id:
            # Count the number of teams in the selected league
            team_count = Team.query.filter_by(league_id=selected_league_id).count()
            # Generate a random draft position between 1 and team_count + 1 (to allow for the new team)
            self.draft_position.data = random.randint(1, team_count + 1)
