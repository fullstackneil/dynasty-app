import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import { useModal } from "../../context/Modal";
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { closeModal } = useModal();
  const sessionUser = useSelector((state) => state.session.user);
  const [first_name, setFirst_Name] = useState("");
  const [last_name, setLast_Name] = useState("");
  const [phone_number, setPhone_Number] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [validations, setValidations] = useState({});


  useEffect(() => {
    let validationsObj = {};
    if (first_name.trim() === "") validationsObj.first_name = "First name is required.";
    if (last_name.trim() === "") validationsObj.last_name = "Last name is required.";
    if (phone_number.trim() === "") validationsObj.phone_number = "Phone Number is required.";
    if (email.trim() === "") validationsObj.email = "Email is required.";
    if (username.trim() === "") validationsObj.username = "Username is required.";
    if (password.trim() === "") validationsObj.password = "Password is required.";
    if (confirmPassword.trim() === "") validationsObj.confirmPassword = "Password confirmation is required.";
    if (password !== confirmPassword) validationsObj.confirmPassword = "Confirm Password field must be the same as the Password field.";
    if (username.length < 4) validationsObj.username = "Username must be at least 4 characters.";
    if (username.length > 50) validationsObj.username = "Username must be within 50 characters.";
    if (password.length < 6) validationsObj.password = "Password must be at least 6 characters.";
    if (password.length > 30) validationsObj.password = "Password must be within 30 characters.";

    setValidations(validationsObj);
  }, [first_name, last_name, phone_number, email, username, password, confirmPassword]);


  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormSubmitted(true); // Mark form as submitted to activate validations

    if (Object.values(validations).length === 0) {
      const serverResponse = await dispatch(
        thunkSignup({
          first_name,
          last_name,
          phone_number,
          email,
          username,
          password,
        })
      );

      if (serverResponse) {
        setValidations(serverResponse);
      } else {
        closeModal();
        navigate("/leagues");
      }
    }
  };

  if (sessionUser) return <Navigate to="/" replace={true} />;

  return (
    <div className='sign-up-form-container'>
      <h1 className='sign-up-form-title'>Sign Up</h1>
      {formSubmitted && validations.server && <p>{validations.server}</p>}
      <form onSubmit={handleSubmit}>
        <div className='sign-up-form-content'>
          <label>
            First Name
            <input
              className='input-section'
              type='text'
              value={first_name}
              onChange={(e) => setFirst_Name(e.target.value)}
              required
            />
          </label>
          {formSubmitted && validations.first_name && <p className='validation-error-msg'>{validations.first_name}</p>}
          <label>
            Last Name
            <input
              className='input-section'
              type='text'
              value={last_name}
              onChange={(e) => setLast_Name(e.target.value)}
              required
            />
          </label>
          {formSubmitted && validations.last_name && <p className='validation-error-msg'>{validations.last_name}</p>}
          <label>
            Phone Number
            <input
              className='input-section'
              type='text'
              value={phone_number}
              onChange={(e) => setPhone_Number(e.target.value)}
              required
            />
          </label>
          {formSubmitted && validations.phone_number && <p className='validation-error-msg'>{validations.phone_number}</p>}
          <label>
            Email
            <input
              className='input-section'
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          {formSubmitted && validations.email && <p className='validation-error-msg'>{validations.email}</p>}
          <label>
            Username
            <input
              className='input-section'
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </label>
          {formSubmitted && validations.username && <p className='validation-error-msg'>{validations.username}</p>}
          <label>
            Password
            <input
              className='input-section'
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          {formSubmitted && validations.password && <p className='validation-error-msg'>{validations.password}</p>}
          <label>
            Confirm Password
            <input
              className='input-section'
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </label>
          {formSubmitted && validations.confirmPassword && <p className='validation-error-msg'>{validations.confirmPassword}</p>}
          <button type="submit" className='submit-button'>Sign Up</button>
        </div>
      </form>
    </div>
  );
}

export default SignupFormPage;
