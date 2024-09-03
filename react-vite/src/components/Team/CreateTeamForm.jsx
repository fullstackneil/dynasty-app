import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useModal } from '../../context/Modal';
import { fetchAllTeamsforLeague, createATeam } from '../../redux/team';
import './CreateTeamForm.css';

const CreateTeamForm = ({ id }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const [name, setName] = useState('');
    const [image, setImage] = useState(null);
    const [imagePreview, setImagePreview] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);
    const [validations, setValidations] = useState({});
    const [formSubmitted, setFormSubmitted] = useState(false);

    const currentUser = useSelector((state) => state.session.user);

    useEffect(() => {
        const validationsObj = {};
        if (!name) validationsObj.name = 'Team name is required.';
        setValidations(validationsObj);
    }, [name]);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        setImage(file);
        setImagePreview(URL.createObjectURL(file)); // Generate a preview URL
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormSubmitted(true);

        if (Object.keys(validations).length === 0) {
            const formData = new FormData();
            formData.append("name", name);
            formData.append("league_id", id);
            formData.append("user_id", currentUser.id);
            if (image) formData.append("image", image);

            setImageLoading(true);

            try {
                dispatch(createATeam(id, formData))
                .then(() => dispatch(fetchAllTeamsforLeague(id)))
                .then(() => closeModal());

                resetFormState();
            } catch (error) {
                console.error('Failed to create team:', error);
                // Optionally, show an error message to the user
            } finally {
                setImageLoading(false);
            }
        }
    };

    const resetFormState = () => {
        setName('');
        setImage(null);
        setImagePreview(null);
        setValidations({});
        setFormSubmitted(false);
    };

    return (
        <form className='team-form-container' encType="multipart/form-data" onSubmit={handleSubmit}>
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
                <label className='team-image-label'>
                    Team Avatar:
                    <input
                        type='file'
                        accept='image/*'
                        onChange={handleImageChange}
                    />
                </label>
                {imagePreview && (
                    <div className='team-image-preview'>
                        <img src={imagePreview} alt='Preview' className='preview-img' />
                    </div>
                )}
                {imageLoading && <p>Loading...</p>}
                <button
                    className='submit-button'
                    type='submit'
                    disabled={imageLoading}
                >
                    {imageLoading ? 'Submitting...' : 'Submit'}
                </button>
            </div>
        </form>
    );
};

export default CreateTeamForm;
