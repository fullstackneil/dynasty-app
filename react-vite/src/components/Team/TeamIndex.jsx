import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllTeamsforLeague } from '../../redux/team';
import { useParams } from 'react-router-dom';
import { useModal } from '../../context/Modal'
import CreateTeamForm from './CreateTeamForm';
import DeleteTeamForm from './DeleteTeamForm';
import UpdateTeamForm from './UpdateTeamForm';
import './TeamIndex.css'

const TeamIndex = () => {
    const dispatch = useDispatch();
    const currentUser = useSelector((state) => state.session.user);
    const allTeamsArr = useSelector((state) => state.team.allTeamsArr);
    const { id } = useParams();
    const { setModalContent } = useModal();

    useEffect(() => {
        dispatch(fetchAllTeamsforLeague(id));
    }, [dispatch, id]);

    if (!currentUser) return null;  // Simplified conditional rendering

    const userHasTeamInLeague = allTeamsArr.some(team => team.user_id === currentUser.id);


    return (
        <>
            <h2 className='team-page-header'>Teams</h2>
            {currentUser && !userHasTeamInLeague && (
                            <div className='create-team-button-container'>
                                <button
                                    className='create-review-button'
                                    onClick={() => setModalContent(<CreateTeamForm id={id}/>)}
                                >Create A Team
                                </button>
                            </div>
            )}
            <div className='team-list-container'>
                {allTeamsArr.length > 0 ? (
                    allTeamsArr.map((team) => (
                        <div key={team.id} className='team-spot-container'>
                            <div className='team-info-text'>
                                <h2>{team.name}</h2>
                                <p>Team Name: {team.name}</p>
                                <p>Draft Position: {team.draft_position}</p>
                                {currentUser?.id === team.user_id && (
                                <>
                                    <button
                                    className='delete-button'
                                    onClick={() => setModalContent(<DeleteTeamForm teamId={team.id} leagueId={team.league_id}/>)}
                                    >
                                    Delete
                                    </button>
                                    <button
                                    className='update-button'
                                    onClick={() => setModalContent(<UpdateTeamForm teamId={team.id} leagueId={team.league_id} />)}
                                    > Edit
                                    </button>
                                </>
                                )}
                            </div>
                        </div>
                    ))
                ) : (
                    <p>No teams available in this league.</p>
                )}
            </div>
        </>
    );
};

export default TeamIndex;
