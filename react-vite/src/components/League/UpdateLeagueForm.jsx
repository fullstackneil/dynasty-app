import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSingleLeague, updateLeague, fetchAllLeagues } from '../../redux/league';
import { useModal } from '../../context/Modal';
import './UpdateLeagueForm.css'

const UpdateLeagueForm = ({ leagueId }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    const [ name, setName ] = useState('')
    const [ draft_type, setDraft_Type ] = useState('')
    const [ scoring_system, setScoring_System ] = useState('')
    const [ max_teams, setMax_Teams ] = useState('');
    const [ validations, setValidations ] = useState({});
    const [ formSubmitted, setFormSubmitted ] = useState(false)

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
        const fetchLeague = async () => {
            const data = await dispatch(fetchSingleLeague(leagueId));
            if (data) {
                setName(data.name)
                setDraft_Type(data.draft_type)
                setScoring_System(data.scoring_system)
                setMax_Teams(data.max_teams)
            }

        }
        fetchLeague();
    }, [dispatch, leagueId])

    useEffect(() => {
        let validationsObj = {};
        if (!name) validationsObj.name = 'League name is required.'
        if (!draft_type) validationsObj.draft_type = 'Draft type is required.'
        if (!scoring_system) validationsObj.scoring_system = 'Scoring system is required.'
        if (!max_teams) validationsObj.max_teams = 'Max teams amount is required.'
        setValidations(validationsObj);
    }, [dispatch, name, draft_type, scoring_system, max_teams])

    const handleSubmit = (e) => {
        e.preventDefault();
        setFormSubmitted(true)

        if (Object.values(validations).length === 0) {

            const newLeague = {
                name,
                draft_type,
                scoring_system,
                max_teams
            }

            dispatch(updateLeague(newLeague, leagueId));
            dispatch(fetchAllLeagues());

            closeModal();

            setValidations({});
            setName('');
            setDraft_Type('');
            setScoring_System('');
            setMax_Teams('')
            setFormSubmitted(false);

        }
    }



    return (
        <form className='update-league-form-container' onSubmit={handleSubmit}>
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
                <label htmlFor='update-league-draft-type-label'>
                    Draft Type:
                    <select className='update-league-draft-type-input'
                            value={draft_type}
                            onChange={(e) => setDraft_Type(e.target.value)}>
                        <option value=''>Please choose an option...</option>
                        {draftTypeOptions}
                    </select>
                </label>
                {formSubmitted && 'draft_type' in validations && <p className='validation-error-msg'>{validations.draft_type}</p>}
                <label htmlFor='update-league-scoring-system-label'>
                    Scoring System:
                    <select className='update-league-scoring-system-input'
                        value={scoring_system}
                        onChange={(e) => setScoring_System(e.target.value)}>
                        <option value=''>Please choose an option...</option>
                        {scoringSystemOptions}
                    </select>
                </label>
                {formSubmitted && 'scoring_system' in validations && <p className='validation-error-msg'>{validations.scoring_system}</p>}
                <label htmlFor='update-league-max-teams-label'>
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
                    Update
                </button>
            </div>
        </form>

    )

}

export default UpdateLeagueForm;
