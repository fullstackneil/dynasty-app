import { useDispatch } from 'react-redux';
import { deleteATeam, fetchAllTeamsforLeague } from '../../redux/team';
import { useModal } from '../../context/Modal';
import './DeleteTeamForm.css';

const DeleteTeamForm = ({ teamId, leagueId }) => {
    const { closeModal } = useModal();
    const dispatch = useDispatch();

    const handleDelete = async () => {
        try {
            await dispatch(deleteATeam(teamId));
            await dispatch(fetchAllTeamsforLeague(leagueId));
            closeModal();
        } catch (error) {
            console.error('Failed to delete team:', error);
            // Optionally, handle the error by showing an error message to the user
        }
    };

    return (
        <div className='delete-team-container'>
            <h2 className='header-title'>Confirm Delete</h2>
            <p className='header-message'>Are you sure you want to delete this team?</p>
            <div className='button-container'>
                <button
                    className='button-content'
                    id='delete-team'
                    onClick={handleDelete}
                >
                    Yes
                </button>
                <button
                    className='button-content'
                    id='keep-team'
                    onClick={closeModal}
                >
                    No
                </button>
            </div>
        </div>
    );
};

export default DeleteTeamForm;
