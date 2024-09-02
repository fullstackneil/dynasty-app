import { useState, useEffect } from "react"
import { useDispatch, useSelector } from 'react-redux';
import { useModal } from '../../context/Modal';
// import { useNavigate } from 'react-router-dom';
import { createALeague, fetchAllLeagues } from "../../redux/league";
// import { createPost } from "../../redux/image";
import './CreateLeagueForm.css'

const CreateLeagueForm = () => {
    const dispatch = useDispatch();
    // const navigate = useNavigate();
    const { closeModal } = useModal();

    const [ name, setName ] = useState('');
    const [ draft_type, setDraft_Type] = useState('');
    const [ scoring_system, setScoring_System ] = useState('');
    const [ max_teams, setMax_Teams ] = useState('');
    const [ image, setImage ]= useState(null);
    const [ imageLoading, setImageLoading ] = useState(false);
    const [ validations, setValidations ] = useState({});
    const [ formSubmitted, setFormSubmitted ] = useState(false);

    const allLeagues = useSelector((state) => state.league.allLeaguesArr)

    // DRAFT TYPE OPTIONS - Displaying various draft options
    const draftTypes = allLeagues.map((league => league.draft_type))
    const uniqueDraftTypes = [...new Set(draftTypes)] // 'Set' creates unique array and removes duplicates
    const draftTypeOptions = uniqueDraftTypes.map((draftType, index) => (
        <option key={index} value={draftType}>
            {draftType}
        </option>
    ))

     // SCORING SYSTEM OPTIONS - Displaying various scoring system options
     const scoringSystems = allLeagues.map((league => league.scoring_system))
     const uniqueScoringSystems = [...new Set(scoringSystems)] // 'Set' creates unique array and removes duplicates
     const scoringSystemOptions = uniqueScoringSystems.map((scoringSystem, index) => (
        <option key={index} value={scoringSystem}>
            {scoringSystem}
        </option>
    ))

    // MAX TEAM OPTIONS - Displaying various max team options
    const maxTeams = allLeagues.map((league => league.max_teams))
    const uniqueMaxTeams = [...new Set(maxTeams)] // 'Set' creates unique array and removes duplicates
    const maxTeamsOptions = uniqueMaxTeams.map((maxTeam, index) => (
        <option key={index} value={maxTeam}>
            {maxTeam}
        </option>
    ))

    useEffect(() => {
        let validationsObj = {};
        if (!name) validationsObj.name = 'League name is required.'
        if (!draft_type) validationsObj.draft_type = 'Draft type is required.'
        if (!scoring_system) validationsObj.scoring_system = 'Scoring system is required.'
        if (!max_teams) validationsObj.max_teams = 'Max teams amount is required.'
        setValidations(validationsObj);
    }, [ name, draft_type, scoring_system, max_teams])



    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormSubmitted(true)

        if (Object.values(validations).length === 0) {
                const formData = new FormData();
                formData.append("name", name);
                formData.append("draft_type", draft_type);
                formData.append("scoring_system", scoring_system);
                formData.append("max_teams", max_teams);
                formData.append("image", image);

                setImageLoading(true);
                await dispatch(createALeague(formData))
                .then(() => dispatch(fetchAllLeagues()))
                .then(() => closeModal())
                setImageLoading(false);

                setValidations({});
                setName('');
                setDraft_Type('');
                setScoring_System('');
                setMax_Teams('')
                setImage(null);
                setFormSubmitted(false);

            }

            // const newLeague = {
            //     name,
            //     draft_type,
            //     scoring_system,
            //     max_teams,
            //     image_url: imageUrl
            // }

        }



    return (
        <form className='league-form-container' encType="multipart/form-data" onSubmit={handleSubmit}>
            <div className='league-form-content'>
                <h2 className='league-form-title'>Create a League</h2>
                <label className='league-name-label'>
                    League Name:
                    <input
                        className='league-name-input'
                        type='text'
                        placeholder='League Name'
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </label>
                {formSubmitted && 'name' in validations && <p className='validation-error-msg'>{validations.name}</p>}
                <label className='league-image-label'>
                    Upload Leage Profile Pic:
                    <input
                        type='file'
                        accept='image/*'
                        onChange={(e) => setImage(e.target.files[0])}
                    />
                </label>
                {imageLoading && <p>Loading...</p>}
                <label htmlFor='league-draft-type-label'>
                    Draft Type:
                    <select className='league-draft-type-input'
                            value={draft_type}
                            onChange={(e) => setDraft_Type(e.target.value)}>
                        <option value=''>Please choose an option...</option>
                        {draftTypeOptions}
                    </select>
                </label>
                {formSubmitted && 'draft_type' in validations && <p className='validation-error-msg'>{validations.draft_type}</p>}
                <label htmlFor='league-scoring-system-label'>
                    Scoring System:
                    <select className='league-scoring-system-input'
                        value={scoring_system}
                        onChange={(e) => setScoring_System(e.target.value)}>
                        <option value=''>Please choose an option...</option>
                        {scoringSystemOptions}
                    </select>
                </label>
                {formSubmitted && 'scoring_system' in validations && <p className='validation-error-msg'>{validations.scoring_system}</p>}
                <label htmlFor='league-max-teams-label'>
                    Max Teams:
                        <select className='league-max-teams-input'
                            value={max_teams}
                            onChange={(e) => setMax_Teams(e.target.value)}>
                            <option value=''>Please choose an option...</option>
                            {maxTeamsOptions}
                        </select>
                </label>
                {formSubmitted && 'max_teams' in validations && <p className='validation-error-msg'>{validations.max_teams}</p>}
                <button className='submit-button' type='submit'>
                    Submit
                </button>
            </div>
        </form>

    )




}

export default CreateLeagueForm;
