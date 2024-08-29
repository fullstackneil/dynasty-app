import {useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux';
import { useModal } from '../../context/Modal';
import { useNavigate } from 'react-router-dom';
import { fetchAllLeagues } from "../../redux/league"
import CreateLeague from './CreateLeague';
// import OwnedLeagues from './OwnedLeagues';
import './LeagueIndex.css'


const LeagueIndex = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { setModalContent } = useModal();
    const currentUser = useSelector((state => state.session.user))
    const allLeagues = useSelector((state) => state.league.allLeaguesArr)

    // const { leagueId } = useParams();

    useEffect(() => {
        dispatch(fetchAllLeagues())
    }, [dispatch])

    return (
        <>
            {currentUser && (
                <>
                    <h2 className='league-page-header'>Leagues</h2>
                    <div className='create-league-button-container'>
                        <button
                            className='create-league-button'
                            onClick={() => setModalContent(<CreateLeague />)}
                        >Create a League
                        </button>
                    </div>
                    <div className='league-list-container'>
                        {allLeagues.length > 0 ? (
                            allLeagues.map((league) => (
                                <div
                                    key={league.id}
                                    onClick={() => navigate(`/leagues/${league.id}/teams`)}
                                    className='league-spot-container'
                                >
                                    <div className='league-info-text'>
                                        <h2>{league.name}</h2>
                                        <p>Draft Type: {league.draft_type}</p>
                                        <p>Scoring: {league.scoring_system}</p>
                                        <p># of Players: {league.max_teams}</p>
                                    </div>
                                </div>
                            ))
                        ) : (
                            <p>No leagues available.</p>
                        )}
                    </div>
                </>
            )}
        </>
    );

}

export default LeagueIndex
