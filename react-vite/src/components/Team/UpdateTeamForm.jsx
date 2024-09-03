import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { updateTeam, fetchSingleTeam, fetchAllTeamsforLeague } from '../../redux/team';
import { useModal } from '../../context/Modal';
import './UpdateTeamForm.css';

const UpdateTeamForm = ({ teamId, leagueId }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    const [name, setName] = useState('');
    const [image, setImage] = useState(null);
    const [imagePreview, setImagePreview] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);
    const [formSubmitted, setFormSubmitted] = useState(false);
    const [validations, setValidations] = useState({});

    const currentUser = useSelector((state) => state.session.user);

    useEffect(() => {
        const fetchTeam = async () => {
            const data = await dispatch(fetchSingleTeam(teamId));
            if (data) {
                setName(data.name); // Set initial team name
                if (data.image) {
                    setImagePreview(data.image); // Set initial image preview if available
                }
            }
        };
        fetchTeam();
    }, [dispatch, teamId]);

    useEffect(() => {
        let validationsObj = {};
        if (!name) validationsObj.name = 'Team name is required.';
        setValidations(validationsObj);
    }, [name]);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setImage(file);
            setImagePreview(URL.createObjectURL(file)); // Generate a preview URL
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormSubmitted(true);

        if (Object.keys(validations).length === 0) {
            const formData = new FormData();
            formData.append("name", name);
            formData.append("league_id", leagueId);
            formData.append("user_id", currentUser.id);
            if (image) formData.append("image", image); // Append the new image file

            setImageLoading(true);

            try {
                dispatch(updateTeam(teamId, formData))
                .then(() => dispatch(fetchAllTeamsforLeague(leagueId)))
                .then(() => closeModal());

                // Reset form state only after successful update
                setName('');
                setImage(null);
                setImagePreview(null);
                setValidations({});
                setFormSubmitted(false);
            } catch (error) {
                console.error('Failed to update team:', error);
                // Optionally, handle the error by showing an error message to the user
            } finally {
                setImageLoading(false);
            }
        }
    };

    return (
        <form className='update-team-form-container' encType="multipart/form-data" onSubmit={handleSubmit}>
            <div className='update-team-content'>
                <h2 className="update-team-title">Update Your Team</h2>
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
                <label className="update-team-image-label">
                    Team Avatar:
                    <input
                        type="file"
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
                    className='update-button'
                    type="submit"
                    disabled={imageLoading}
                >
                    {imageLoading ? 'Updating...' : 'Update Your Team'}
                </button>
            </div>
        </form>
    );
};

export default UpdateTeamForm;
