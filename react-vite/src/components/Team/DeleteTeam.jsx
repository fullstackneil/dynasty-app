import { useDispatch } from "react-redux";

import { deleteATeam, fetchAllTeamsforLeague } from "../../redux/team";
import { useModal } from "../../context/Modal";
import './DeleteTeam.css'

const DeleteTeam = ({ teamId, leagueId }) => {

    const { closeModal } = useModal();
    const dispatch = useDispatch();


    const handleDelete = () => {
        dispatch(deleteATeam(teamId))
        closeModal();
        dispatch(fetchAllTeamsforLeague(leagueId))
    }

    return (
        <div className='delete-review-container'>
          <h2 className='header-title'>Confirm Delete</h2>
          <p className='header-message'>Are you sure you want to delete this review?</p>
          <div className='button-container'>
            <button className='button-content' id='delete-review' onClick={handleDelete}>Yes</button>
            <button className='button-content' id='keep-review' onClick={closeModal}>No</button>
          </div>
        </div>
      );

}

export default DeleteTeam;
