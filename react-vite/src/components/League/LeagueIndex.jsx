import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useModal } from '../../context/Modal';
import { useNavigate } from 'react-router-dom';
import { fetchAllLeagues } from "../../redux/league";
import CreateLeagueForm from './CreateLeagueForm';
import DeleteLeagueForm from './DeleteLeagueForm';
import UpdateLeagueForm from './UpdateLeagueForm';
import './LeagueIndex.css';

const LeagueIndex = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { setModalContent } = useModal();
    const currentUser = useSelector(state => state.session.user);
    const allLeagues = useSelector(state => state.league.allLeaguesArr);

    useEffect(() => {
        dispatch(fetchAllLeagues());
    }, [dispatch]);

    return (
        <>
            {currentUser && (
                <>
                    <h2 className='league-page-header'>Leagues</h2>
                    <div className='create-league-button-container'>
                        <button
                            className='create-league-button'
                            onClick={() => setModalContent(<CreateLeagueForm />)}
                        >
                            Create a League
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
                                        <h2 className='league-name-text'>{league.name}</h2>
                                        <p className='draft-type-text'>Draft Type: {league.draft_type}</p>
                                        <p className='scoring-text'>Scoring: {league.scoring_system}</p>
                                        <p className='max-teams-text'># of Players: {league.max_teams}</p>
                                        {currentUser?.id === league.commissioner_id && (
                                            <>
                                                <button
                                                    className='update-button'
                                                    onClick={(e) => {
                                                        e.stopPropagation();
                                                        setModalContent(<UpdateLeagueForm leagueId={league.id} />);
                                                    }}
                                                >
                                                    Edit
                                                </button>
                                                <button
                                                    className='delete-button'
                                                    onClick={(e) => {
                                                        e.stopPropagation();
                                                        setModalContent(<DeleteLeagueForm leagueId={league.id} />);
                                                    }}
                                                >
                                                    Delete
                                                </button>
                                            </>
                                        )}
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
};

export default LeagueIndex;
