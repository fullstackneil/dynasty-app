import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import UploadPicture from '../components/UploadPicture/UploadPicture'
import League from '../components/League/League';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: '/leagues',
        element: <League />,
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
