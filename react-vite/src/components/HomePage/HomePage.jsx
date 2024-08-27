// import { useEffect, useState } from 'react';
// import { useDispatch } from 'react-redux';
// import { useParams } from 'react-router-dom';
// import { useModal } from '../../context/Modal';
import LoginFormPage from '../LoginFormPage/LoginFormPage';
import SignupFormPage from '../SignupFormPage/SignupFormPage';

const HomePage = () => {
    return (
        <div className="login-signup-container">
            <LoginFormPage />
            <SignupFormPage />
        </div>
    )
}

export default HomePage
