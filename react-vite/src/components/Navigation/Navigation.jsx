import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import logo from '../../../assets/dynasty-app.svg'
import "./Navigation.css";

function Navigation() {
  return (
    <nav className='navbar-container'>
      <NavLink className='logo-container' to="/leagues">
        <img src={logo} alt="Home" className="navbar-logo" />
      </NavLink>
      <NavLink className='nav-link' to='/leagues'>
        Leagues
      </NavLink>
      <NavLink className='nav-link' to='/teams'>
        Teams
      </NavLink>
      <NavLink className='nav-link' to='/players'>
        Player Rankings
      </NavLink>
      <NavLink className='nav-link' to='/draft'>
        Draft
      </NavLink>
      <div className='nav-btn-holder'>
        <ProfileButton />
      </div>
    </nav>
  );
}

export default Navigation;
