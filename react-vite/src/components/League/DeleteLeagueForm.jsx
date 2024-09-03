import { useDispatch } from 'react-redux';
import { useModal } from '../../context/Modal';
import { deleteALeague, fetchAllLeagues } from '../../redux/league';
import './DeleteLeagueForm.css'


const DeleteLeagueForm = ({leagueId}) => {

    const { closeModal } = useModal();
    const dispatch = useDispatch();

    const handleDelete = () => {
      dispatch(deleteALeague(leagueId))
      .then(dispatch(fetchAllLeagues()))
      .then(() => closeModal())
    }

    return (
        <div className='delete-league-container'>
          <h2 className='header-title'>Confirm Delete</h2>
          <p className='header-message'>Are you sure you want to delete this league?</p>
          <div className='button-container'>
            <button className='button-content' id='delete-league' onClick={handleDelete}>Yes</button>
            <button className='button-content' id='keep-league' onClick={closeModal}>No</button>
          </div>
        </div>
    );

}

export default DeleteLeagueForm;
