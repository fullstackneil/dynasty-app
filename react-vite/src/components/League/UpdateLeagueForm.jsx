import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSingleLeague, updateLeague, fetchAllLeagues } from '../../redux/league';
import { useModal } from '../../context/Modal';
import './UpdateLeagueForm.css';

const UpdateLeagueForm = ({ leagueId }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const [name, setName] = useState('');
    const [draft_type, setDraft_Type] = useState('');
    const [scoring_system, setScoring_System] = useState('');
    const [max_teams, setMax_Teams] = useState('');
    const [image, setImage] = useState(null);
    const [imagePreview, setImagePreview] = useState(null); // Preview URL for image
    const [validations, setValidations] = useState({});
    const [formSubmitted, setFormSubmitted] = useState(false);

    const allLeagues = useSelector((state) => state.league.allLeaguesArr);

    // DRAFT TYPE OPTIONS - Displaying various draft options
    const draftTypes = allLeagues.map((league) => league.draft_type);
    const uniqueDraftTypes = [...new Set(draftTypes)];
    const draftTypeOptions = uniqueDraftTypes.map((draftType, index) => (
        <option key={index} value={draftType}>
            {draftType}
        </option>
    ));

    // SCORING SYSTEM OPTIONS - Displaying various scoring system options
    const scoringSystems = allLeagues.map((league) => league.scoring_system);
    const uniqueScoringSystems = [...new Set(scoringSystems)];
    const scoringSystemOptions = uniqueScoringSystems.map((scoringSystem, index) => (
        <option key={index} value={scoringSystem}>
            {scoringSystem}
        </option>
    ));

    // MAX TEAM OPTIONS - Displaying various max team options
    const maxTeams = allLeagues.map((league) => league.max_teams);
    const uniqueMaxTeams = [...new Set(maxTeams)];
    const maxTeamsOptions = uniqueMaxTeams.map((maxTeam, index) => (
        <option key={index} value={maxTeam}>
            {maxTeam}
        </option>
    ));

    useEffect(() => {
        const fetchLeague = async () => {
            const data = await dispatch(fetchSingleLeague(leagueId));
            if (data) {
                setName(data.name);
                setDraft_Type(data.draft_type);
                setScoring_System(data.scoring_system);
                setMax_Teams(data.max_teams);
                if (data.image_url) {
                    setImagePreview(data.image_url); // Set existing image URL for preview
                }
            }
        };
        fetchLeague();
    }, [dispatch, leagueId]);

    useEffect(() => {
        let validationsObj = {};
        if (!name) validationsObj.name = 'League name is required.';
        if (!draft_type) validationsObj.draft_type = 'Draft type is required.';
        if (!scoring_system) validationsObj.scoring_system = 'Scoring system is required.';
        if (!max_teams) validationsObj.max_teams = 'Max teams amount is required.';
        setValidations(validationsObj);
    }, [name, draft_type, scoring_system, max_teams]);

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        setImage(file);
        setImagePreview(URL.createObjectURL(file)); // Generate preview URL
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormSubmitted(true);

        if (Object.values(validations).length === 0) {
            const formData = new FormData();
            formData.append("name", name);
            formData.append("draft_type", draft_type);
            formData.append("scoring_system", scoring_system);
            formData.append("max_teams", max_teams);
            if (image) formData.append("image", image);

            try {
                dispatch(updateLeague(formData, leagueId))
                .then(() => dispatch(fetchAllLeagues()))
                .then(() => closeModal());
                resetFormState();
            } catch (error) {
                console.error("Failed to update league:", error);
            } finally {
                setFormSubmitted(false);
            }
        }
    };

    const resetFormState = () => {
        setName('');
        setDraft_Type('');
        setScoring_System('');
        setMax_Teams('');
        setImage(null);
        setImagePreview(null);
        setValidations({});
        setFormSubmitted(false);
    };

    return (
        <form className='update-league-form-container' encType="multipart/form-data" onSubmit={handleSubmit}>
            <div className='update-league-form-content'>
                <h2 className='update-league-form-title'>Update League</h2>
                <label className='update-league-name-label'>
                    League Name:
                    <input
                        className='update-league-name-input'
                        type='text'
                        placeholder='League Name'
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </label>
                {formSubmitted && 'name' in validations && <p className='validation-error-msg'>{validations.name}</p>}
                <label className='update-league-image-label'>
                    League Avatar:
                    <input
                        type='file'
                        accept='image/*'
                        onChange={handleImageChange}
                    />
                </label>
                {imagePreview && (
                    <div className='image-preview'>
                        <img src={imagePreview} alt='Preview' className='preview-img' />
                    </div>
                )}
                <label htmlFor='update-league-draft-type-label'>
                    Draft Type:
                    <select
                        className='update-league-draft-type-input'
                        value={draft_type}
                        onChange={(e) => setDraft_Type(e.target.value)}
                    >
                        <option value=''>Please choose an option...</option>
                        {draftTypeOptions}
                    </select>
                </label>
                {formSubmitted && 'draft_type' in validations && <p className='validation-error-msg'>{validations.draft_type}</p>}
                <label htmlFor='update-league-scoring-system-label'>
                    Scoring System:
                    <select
                        className='update-league-scoring-system-input'
                        value={scoring_system}
                        onChange={(e) => setScoring_System(e.target.value)}
                    >
                        <option value=''>Please choose an option...</option>
                        {scoringSystemOptions}
                    </select>
                </label>
                {formSubmitted && 'scoring_system' in validations && <p className='validation-error-msg'>{validations.scoring_system}</p>}
                <label htmlFor='update-league-max-teams-label'>
                    Max Teams:
                    <select
                        className='league-max-teams-input'
                        value={max_teams}
                        onChange={(e) => setMax_Teams(e.target.value)}
                    >
                        <option value=''>Please choose an option...</option>
                        {maxTeamsOptions}
                    </select>
                </label>
                {formSubmitted && 'max_teams' in validations && <p className='validation-error-msg'>{validations.max_teams}</p>}
                <button className='submit-button' type='submit'>
                    Update
                </button>
            </div>
        </form>
    );
};

export default UpdateLeagueForm;
