import {React, useState, useEffect, useContext} from "react";
import { useNavigate, NavLink, useParams } from 'react-router-dom';
import AuthContext from "../context/AuthContext";
import { Formik } from 'formik';
import * as Yup from 'yup';
import '../styles/forms.css';


const validationSchema = Yup.object().shape({
    name: Yup.string()
    .required("Nazwa jest wymagana."),
    address: Yup.string()
    .required("Adres jest wymagany."),
  });

const PublicGyms = () => {
    let [gymList, setGymList] = useState([]);
    let {authTokens, user} = useContext(AuthContext)

    useEffect(() => {
        getSharedGymsList()
    }, [])

    let getSharedGymsList = async() => {
        let response = await fetch('http://localhost:8000/api/user/gyms/sharedlist/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        setGymList(data)
    }

    return (
        <div className="col-12 col-md-12 ">
            <p className="h1 text-center">Udostępnione siłownie</p>
            <div className="row">
            {gymList.map((gym, index) => (
                <div key={index} className="text-center col-12 col-sm-6 col-md-4 my-2 py-3 bg-light border">
                    <NavLink to={'/gyms/shared/'+gym.id} className="nav-link">
                        <p className="h3">{gym.name}</p>
                        <p className="h6">{gym.addres}</p>
                    </NavLink>
                </div>
                ))}
            </div>
        </div>
    )

}

export default PublicGyms