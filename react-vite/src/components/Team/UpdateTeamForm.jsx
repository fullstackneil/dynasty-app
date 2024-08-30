import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { updateTeam, fetchSingleTeam, fetchAllTeamsforLeague } from '../../redux/team';
import { useModal } from '../../context/Modal';
import './UpdateTeamForm.css'

const UpdateTeamForm = ({ teamId, leagueId }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    const [name, setName] = useState('');
    const [formSubmitted, setFormSubmitted] = useState(true);
    const [validations, setValidations] = useState({});

    const currentUser = useSelector((state) => state.session.user);

    useEffect(() => {
        const fetchTeam = async () => {
            const data = await dispatch(fetchSingleTeam(teamId));
            if (data) {
                setName(data.name); // Set initial team name
            }
        };
        fetchTeam();
    }, [dispatch, teamId]);

    useEffect(() => {
        let validationsObj = {};
        if (!name) validationsObj.name = 'Team name is required.';
        setValidations(validationsObj);
    }, [name]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (Object.values(validations).length === 0) {
            const newTeam = {
                name,
                league_id: leagueId,
                user_id: currentUser.id,
            };

            await dispatch(updateTeam(teamId, newTeam));
            await dispatch(fetchAllTeamsforLeague(leagueId));

            closeModal();

            setName('');
            setValidations({});
            setFormSubmitted(false);
        } else {
            setFormSubmitted(true);
        }
    };

    return (
        <form className='update-team-form-container' onSubmit={handleSubmit}>
            <div className='update-team-content'>
                <h2 className="update-team-title">Change Your Team Name?</h2>
                {formSubmitted && 'name' in validations && <p className="validation-error-msg">{validations.name}</p>}
                <label className="update-team-label">
                    New Team Name:
                    <input
                        type="text"
                        placeholder="Team Name"
                        className="team-input"
                        id='input-text-box'
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </label>
                <button
                    className='update-button'
                    type="submit"
                >
                    Update Your Team
                </button>
            </div>
        </form>
    );
};

export default UpdateTeamForm;
