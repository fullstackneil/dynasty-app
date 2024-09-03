import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { useModal } from '../../context/Modal';
import { fetchAllPlayers } from "../../redux/player";
import './PlayerIndex.css'

const PlayerIndex = () => {
    const dispatch = useDispatch();

    const currentUser = useSelector(state => state.session.user);
    const allPlayers = useSelector(state => state.player.allPlayersArr);

    useEffect(() => {
        dispatch(fetchAllPlayers());
    }, [dispatch])


    return (
        <>
            {currentUser && (
                <>
                    <h2 className='player-page-header'>Player Rankings</h2>
                    <div className='player-list-container'>
                        {allPlayers.length > 0 ? (
                            allPlayers.map((player) => (
                                <div
                                    key={player.id}
                                    className='player-spot-container'
                                >
                                    <div className='player-details-container'>
                                        <div className='player-ranking-container'>
                                            <h1 className='player-ranking'>{player.id}</h1>
                                        </div>

                                        {player.image_url && (
                                            <div className='player-image-container'>
                                                <img src={player.image_url} alt={`${player.first_name} ${player.last_name}`} className='player-image' />
                                            </div>
                                        )}
                                        <div className='player-info-text'>
                                            <h2 className='player-name-text'>
                                                {player.first_name} {player.last_name}
                                            </h2>
                                            <p className='player-position'>{player.position}</p>
                                            <p className='player-team'>{player.team}</p>
                                            <p className='player-adp'>Average Draft Position: {player.average_draft_position}</p>
                                            <p className='player-points-last-season'>Points Last Season {player.points_last_season}</p>
                                        </div>
                                    </div>
                                </div>
                            ))
                        ) : (
                            <p>No Players Available</p>
                        )}
                    </div>
                </>
            )}
        </>
    );


}

export default PlayerIndex
