import {React, useState, useEffect, useContext} from "react";
import { useNavigate, NavLink } from 'react-router-dom';
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

const UserGymListPage = () => {
    let [userGyms, setUserGyms] = useState([]);
    let {authTokens} = useContext(AuthContext)

    useEffect(() => {
        getUserGymsData()
    }, [])

    let getUserGymsData = async() => {
        let response = await fetch('http://localhost:8000/api/user/gyms/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        setUserGyms(data)
    }

    return (
        <div className="container-fluid mt-3">
            <div className="row">
                <div className="col-12 col-md-6 text-center">
                    <p className="h1">Twoje siłownie</p>
                    {userGyms.map((gym, index) => (
                    <NavLink to={'/gyms/'+gym.id} className="nav-link">
                        <div key={index} className="text-center col-12 col-sm-6 col-md-4 my-2 py-3 bg-light border">
                            <p className="h3">{gym.gym_name}</p>
                            <p className="h6">{gym.address}</p>
                        </div>
                    </NavLink>
                    ))}
                </div>
                <div className="col-12 col-md-6">
                <p className="h1 text-center">Dodaj nową siłownie</p>
                    <Formik
                    initialValues={{name: "", address: ""}}
                    validationSchema={validationSchema}
                    onSubmit={(values, {setSubmitting, resetForm}) => {
                        setSubmitting(true);
                        resetForm();
                        setSubmitting(false);
                    }}>
                    {( {values,
                        errors,
                        touched,
                        handleChange,
                        handleBlur,
                        handleSubmit,
                        isSubmitting }) => (
                        <form onSubmit={handleSubmit}>
                            <div className='mb-3'>
                                <label htmlFor="name" className="form-label">Nazwa</label>
                                <input
                                    type="text"
                                    name="name"
                                    placeholder="Nazwa"
                                    id="name"
                                    onChange={handleChange}
                                    onBlur={handleBlur}
                                    value={values.name}
                                    className={`${touched.name && errors.name ? 'error' : null} form-control`}
                                />
                                {touched.name && errors.name ? (
                                <div className="error-message">{errors.name}</div>
                                ): null}
                            </div>
                            <div className='mb-3'>
                                <label htmlFor="address" className="form-label">Adres</label>
                                <input
                                    type="text"
                                    name="address"
                                    placeholder="Adres"
                                    id="address"
                                    onChange={handleChange}
                                    onBlur={handleBlur}
                                    value={values.height}
                                    className={`${touched.address && errors.address ? 'error' : null} form-control`}
                                />
                                {touched.address && errors.address ? (
                                <div className="error-message">{errors.address}</div>
                                ): null}
                            </div>
                            <button className="btn btn-primary" type="submit" disabled={isSubmitting}>Dodaj</button>
                        </form>
                    )}
                    </Formik>
                </div>
            </div>
        </div>
    )

}

export default UserGymListPage