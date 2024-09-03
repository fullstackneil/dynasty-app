import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useModal } from '../../context/Modal';
import { fetchAllTeamsforLeague, createATeam } from '../../redux/team';
import './CreateTeamForm.css';

const CreateTeamForm = ({ id }) => {
    const [name, setName] = useState('');
    const [validations, setValidations] = useState({});
    const [formSubmitted, setFormSubmitted] = useState(false);

    const { closeModal } = useModal();
    const dispatch = useDispatch();
    const currentUser = useSelector((state) => state.session.user);

    useEffect(() => {
        const validationsObj = {};
        if (!name) validationsObj.name = 'Team name is required.';
        setValidations(validationsObj);
    }, [name]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormSubmitted(true);

        if (Object.keys(validations).length === 0) {
            const newTeam = {
                name,
                league_id: id,
                user_id: currentUser.id,
            };

            try {
                dispatch(createATeam(id, newTeam))
                .then(() => dispatch(fetchAllTeamsforLeague(id)))
                .then(() => closeModal());
                
                setName('');
                setValidations({});
                setFormSubmitted(false);
            } catch (error) {
                console.error('Failed to create team:', error);
                // Optionally, handle the error by showing an error message to the user
            }
        }
    };

    return (
        <form className='team-form-container' onSubmit={handleSubmit}>
            <div className='team-form-content'>
                <h2 className='team-form-title'>Create a Team</h2>
                <label className='team-label'>
                    <input
                        className='input-area-team-name'
                        type='text'
                        placeholder='Team Name'
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </label>
                {formSubmitted && validations.name && (
                    <p className='name-validation-error'>{validations.name}</p>
                )}
                <button className='submit-button' type='submit'>
                    Submit
                </button>
            </div>
        </form>
    );
};

export default CreateTeamForm;
