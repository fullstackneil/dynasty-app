// import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
// import { useDispatch } from 'react-redux';
// import { useParams } from 'react-router-dom';
// import { useModal } from '../../context/Modal';
import LoginFormPage from '../LoginFormPage/LoginFormPage';
// import SignupFormPage from '../SignupFormPage/SignupFormPage';
import './HomePage.css';

const HomePage = () => {
    const currentUser = useSelector((state)=> state.session.user);

    return (
        <div className="home-page">
            {!currentUser ? (
                <>
                    <LoginFormPage />
                </>
            ): (
                <>
                </>
            )
            }
        </div>
    )
}

export default HomePage
