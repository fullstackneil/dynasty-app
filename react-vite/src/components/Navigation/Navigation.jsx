import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import logo from '../../../dist/assets/dynasty-app.svg'
import "./Navigation.css";

function Navigation() {
  return (
    <nav className='navbar-container'>
      <NavLink className='logo-container' to="/">
        <img src={logo} alt="Home" className="navbar-logo" />
      </NavLink>
      {/* <NavLink to='/teams'>
        Teams
      </NavLink> */}
      <div className='nav-btn-holder'>
        <ProfileButton />
      </div>
    </nav>
  );
}

export default Navigation;
