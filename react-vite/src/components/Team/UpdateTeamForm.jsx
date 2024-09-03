import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { updateTeam, fetchSingleTeam, fetchAllTeamsforLeague } from '../../redux/team';
import { useModal } from '../../context/Modal';
import './UpdateTeamForm.css';

const UpdateTeamForm = ({ teamId, leagueId }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    const [name, setName] = useState('');
    const [formSubmitted, setFormSubmitted] = useState(false);
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
        setFormSubmitted(true);

        if (Object.keys(validations).length === 0) {
            const updatedTeam = {
                name,
                league_id: leagueId,
                user_id: currentUser.id,
            };

            try {
                await dispatch(updateTeam(teamId, updatedTeam));
                await dispatch(fetchAllTeamsforLeague(leagueId));
                closeModal();

                // Reset form state only after successful update
                setName('');
                setValidations({});
                setFormSubmitted(false);
            } catch (error) {
                console.error('Failed to update team:', error);
                // Optionally, handle the error by showing an error message to the user
            }
        }
    };

    return (
        <form className='update-team-form-container' onSubmit={handleSubmit}>
            <div className='update-team-content'>
                <h2 className="update-team-title">Change Your Team Name?</h2>
                {formSubmitted && validations.name && (
                    <p className="validation-error-msg">{validations.name}</p>
                )}
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
                <button className='update-button' type="submit">
                    Update Your Team
                </button>
            </div>
        </form>
    );
};

export default UpdateTeamForm;
