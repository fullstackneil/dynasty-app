import {useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux';
// import { getAllLeagues } from '../../redux/league';
import { useNavigate } from 'react-router-dom';
import { fetchAllLeagues } from "../../redux/league"
// import OwnedLeagues from './OwnedLeagues';
import './League.css'


const League = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const currentUser = useSelector((state => state.session.user))
    const allLeagues = useSelector((state) => state.league.allLeaguesArr)

    useEffect(() => {
        dispatch(fetchAllLeagues())
    }, [dispatch])

    return (
        <>
            {currentUser && (
                <>
                    <h2 className='league-page-header'>Leagues</h2>
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

export default League
