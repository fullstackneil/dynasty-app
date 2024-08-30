import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import logo from '../../../assets/dynasty-app.svg'
import "./LoginForm.css";

function LoginFormPage() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [ demo, setDemo ] = useState(false)
  const [errors, setErrors] = useState({});

  if (sessionUser) return <Navigate to="/" replace={true} />;

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      navigate("/leagues");
    }
  };


  const handleDemoUser = async (e) => {
    e.preventDefault();
    setDemo(true);

    if (demo) {
      const demoCredentials = {
        email: "john.doe@example.com",
        password: "password"
      }

      const serverResponse = await dispatch(thunkLogin(demoCredentials))

      if (serverResponse) {
        setErrors(serverResponse);
      } else {
        navigate('/leagues');
      }

      setErrors({})
      setDemo(false)

    }
  }

  return (
    <>
      {/* <h1>Log In</h1> */}
      {errors.length > 0 &&
        errors.map((message) => <p key={message} className='error-message'>{message}</p>)}
      <form onSubmit={handleSubmit} className="form-content">
        <img src={logo} alt="Dynasty App Logo" className="logo" />
        <label className='email-text'>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className='input-text'
          />
        </label>
        {errors.email && <p className='error-message'>{errors.email}</p>}
        <label className='credential-text'>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className='password-text'
          />
        </label>
        {errors.password && <p className='error-message'>{errors.password}</p>}
        <button type="submit" className='button-text'>Log In</button>
        <button className='demo-user-container' id='demo-user-container'
          type='submit'
          onClick={handleDemoUser}
          >Log in as Demo User
        </button>
      </form>
    </>
  );
}

export default LoginFormPage;
