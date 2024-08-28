import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import UploadPicture from '../components/UploadPicture/UploadPicture'
import League from '../components/League/League';
import HomePage from '../components/HomePage/HomePage'
import TeamIndex from '../components/Team/TeamIndex';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "/login",
        element: <LoginFormPage />,
      },
      {
        path: "/signup",
        element: <SignupFormPage />,
      },
      {
        path: "/leagues/",
        element: <League />,
      },
      {
        path: "/leagues/:id/teams",
        element: <TeamIndex />
      },
      {
        path: "/images",
        element: <UploadPicture />,
      },
      // {
      //   path: "/leagues",
      //   element: <League />,
      // }
    ],
  },
]);
