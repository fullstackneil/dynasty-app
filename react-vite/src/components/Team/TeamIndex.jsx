import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllTeamsforLeague } from '../../redux/team';
import { useParams } from 'react-router-dom';
import { useModal } from '../../context/Modal'
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

    return (
        <>
            <h2 className='team-page-header'>Teams</h2>

            {currentUser && (
                <div className='create-button-container'>
                    <button
                        className='create-review-button'
                        onClick={() => setModalContent(<CreateTeam id={id}/>)}
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
