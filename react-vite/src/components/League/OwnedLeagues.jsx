import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
// import { useModal } from '../../context/Modal';
import { fetchAllLeagues } from '../../redux/league';



const OwnedLeagues = ({id}) => {
    const dispatch = useDispatch();
    // const { setModalContent, closeModal } = useModal()

    const allLeagues = useSelector((state) => state.league.allLeaguesArr);
    const currentUser = useSelector((state) => state.session.user);
    const allTeams = useSelector((state) => state.team.allTeamsArr)

    useEffect(() => {
        dispatch(fetchAllLeagues(id))
    }, [dispatch, id])

    const ownedLeagues = allLeagues.filter((league => league)
    );

    console.log('>>>>>>>>>>>>>>>>>>>>>', ownedLeagues)

    const isOwner = currentUser && currentUser.id === allLeagues.id

    return (
        <div className='league-container'>
            <h2>My Leagues</h2>

            {ownedLeagues.map((league) => (
                <div key={league.id} className='league-structure'>
                    {isOwner && (
                        <div className='league-information'>
                            <h3 className='league-name'>{league.name}</h3>
                            <h3 className='league-draft-type'>{league.draft_type}</h3>
                        </div>
                    )}
                </div>
            ))}
        </div>
    );




}

export default OwnedLeagues
