import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useModal } from '../../context/Modal';
import { fetchAllTeamsforLeague, createATeam } from '../../redux/team';

const CreateTeam = ({id}) => {
    const [name, setName] = useState('')
    const [validations, setValidations] = useState({})
    const [formSubmitted, setFormSubmitted] = useState(false)

    const { closeModal } = useModal();
    const dispatch = useDispatch();
    // const navigate = useNavigate();


    const currentUser = useSelector((state)=> state.session.user)

    useEffect(() => {
        let validationsObj = {};
        if (!name) validationsObj.name = "Team name is required."
        setValidations(validationsObj)
    }, [dispatch, name])

    const handleSubmit = async(e) => {
        e.preventDefault();
        setFormSubmitted(true)

        if (Object.values(validations).length === 0) {

            const newTeam = {
                name,
                league_id: id,
                user_id: currentUser.id
            }

            await dispatch(createATeam(id, newTeam))
            await dispatch(fetchAllTeamsforLeague(id))

            closeModal();


            setName('')
            setValidations({})
            setFormSubmitted(false)
        }
    }

    return (
        <form className='team-form' onSubmit={handleSubmit}>
            <h2 className="team-form-title">Create a Team</h2>
            <label className='team-label'>
                Team Name:
                <input
                    className='input-area-team-name'
                    type='text'
                    placeholder='Team Name'
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </label>
            {formSubmitted && 'name' in validations && <p className="name-validation-error">{validations.name}</p>}
            <button className='submit-button' type='submit'>
                Submit
            </button>
        </form>
    )

}


export default CreateTeam;
