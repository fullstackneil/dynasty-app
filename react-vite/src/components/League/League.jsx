import {useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux';
// import { getAllLeagues } from '../../redux/league';
import { useParams } from 'react-router-dom';
import { fetchAllLeagues } from "../../redux/league"
import OwnedLeagues from './OwnedLeagues';



const League = () => {
    const dispatch = useDispatch();
    const {id} = useParams();

    // const allLeagues = useSelector((state) => state.league.allLeaguesArr)
    const currentUser = useSelector((state => state.session.user))

    // useEffect(() => {
    //     dispatch(fetchAllLeagues())
    // }, [dispatch])

    return (
        <>
            {currentUser &&
            <div className='league-container'>
                <h1 className='league-page-header'>Leagues</h1>
                <OwnedLeagues id={id} />
            </div>
            }
        </>
    )
}


export default League
