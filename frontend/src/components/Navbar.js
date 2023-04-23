import React, { useContext } from 'react';
import { useNavigate, NavLink } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

const NavbarComponent = () => {
    const navigate = useNavigate();
    let {user, logoutUser} = useContext(AuthContext)

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
        <NavLink className="navbar-brand" role="button" to='/'>TrainEverywhere</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
            {user ? (
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                    <li className="nav-item" role="button">
                        <NavLink activeClassName="active" exact className="nav-link" to='/'>Home</NavLink>
                    </li>
                    <li className="nav-item" role="button">
                        <NavLink activeClassName="active" className="nav-link" to='/gyms'>Twoje siłownie</NavLink>
                    </li>
                    <li className="nav-item" role="button">
                        <NavLink activeClassName="active" className="nav-link" to='/workouts'>Twoje treningi</NavLink>
                    </li>
                </ul>
            ) : (
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                    <li className="nav-item" role="button">
                        <NavLink activeClassName="active" exact className="nav-link" to='/'>Home</NavLink>
                    </li>
                </ul>
            )}
            {!user ? (
                <ul className="navbar-nav">
                    <li className="nav-item" role="button">
                        <NavLink activeClassName="active" exact className="nav-link" to='/login'>Zaloguj</NavLink>
                    </li>
                    <li className="nav-item" role="button">
                        <NavLink activeClassName="active" className="nav-link" to='/register'>Zarejestruj</NavLink>
                    </li>
                </ul>
            ) : (
                <ul className="navbar-nav">
                    <li className="nav-item" role="button">
                        <NavLink activeClassName="active" exact className="nav-link" to='/user'>Profil</NavLink>
                    </li>
                    <li className="nav-item" role="button">
                        <a className="nav-link" onClick={logoutUser}>Wyloguj</a>
                    </li>
                </ul>
                
            )}
        </div>
        </div>
        </nav>
      );
};

export default NavbarComponent;