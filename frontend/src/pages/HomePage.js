import {React, useContext} from 'react';
import '../styles/home.css';
import AuthContext from '../context/AuthContext';

const HomePage = () => {
    let {user} = useContext(AuthContext)

    return (
        <div className='container-fluid'>
            <div className='row bg_photo justify-content-center'>
                <div className='col-lg-10 py-5 text-center'>
                <h1 className='display-1 text-secondary mb-5 text-center'>
                    TrainEverywhere
                </h1>
                <h3 className='text-secondary text-center fw-light'>
                    Dzięki funkcjonalnościom aplikacji TrainEverywhere trenowanie stanie się znacznie łatwiejsze.
                </h3>
                <ul className='text-secondary baner_list mt-5 fw-bold'>
                    <li >Układanie planów pod twoje wymagania</li>
                    <li>Dodawanie własnych ćwiczeń</li>
                    <li>Tworzenie lokalizacji ze sprzętem</li>
                </ul>
                </div>
            </div>
        </div>
    );
};

export default HomePage;