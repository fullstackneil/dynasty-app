import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import UploadPicture from '../components/UploadPicture/UploadPicture'
import LeagueIndex from '../components/League/LeagueIndex';
import HomePage from '../components/HomePage/HomePage'
import TeamIndex from '../components/Team/TeamIndex';
import PlayerIndex from '../components/Player/PlayerIndex';
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
        element: <LeagueIndex />,
      },
      {
        path: "/leagues/:id/teams",
        element: <TeamIndex />
      },
      {
        path: "/images",
        element: <UploadPicture />,
      },
      {
        path: "/players",
        element: <PlayerIndex />,
      }
    ],
  },
]);
