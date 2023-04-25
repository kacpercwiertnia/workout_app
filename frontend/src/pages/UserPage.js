import {React, useState, useEffect, useContext} from "react";
import AuthContext from "../context/AuthContext";
import { Formik } from 'formik';
import * as Yup from 'yup';
import '../styles/forms.css';

const ageValidation = /^(1[5-9]|[2-9][0-9]|100)$/
const heightValidation = /^(10[0-9]|1[1-9][0-9]|2[0-5][0-9]|260)$/
const weightValidation = /^(4[0-9]|[5-9][0-9]|1[0-9]{2}|200)$/

const validationSchema = Yup.object().shape({
    age: Yup.string()
    .required("Wiek jest wymagany.")
    .matches(ageValidation, "Wiek musi być liczbą od 15 do 100"),
    height: Yup.string()
    .required("Wzrost jest wymagany.")
    .matches(heightValidation, "Wzrost musi być liczbą od 100 do 260"),
    weight: Yup.string()
    .required("Waga jest wymagana.")
    .matches(weightValidation, "Wzrost musi być liczbą od 40 do 200"),
    experience: Yup.string()
    .required("Poziom doświadczenia jest wymagany.")
  });

const UserPage = () => {
    let [userData, setUserData] = useState({});
    let {authTokens, setUserInfo} = useContext(AuthContext)

    useEffect(() => {
        getUserData()
    }, [])

    let getUserData = async() => {
        let response = await fetch('http://localhost:8000/api/user/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        setUserData(data)
    }

    return (
        <div className='container mt-3'>
            <div className='row justify-content-center'>
                <div className='col-12 col-sm-8 col-md-6'>
                <Formik
                initialValues={{age: userData.age ? userData.age : "", height: userData.height ? userData.height : "", weight: userData.weight ? userData.weight : "", experience: userData.experience ? userData.experience : ""}}
                validationSchema={validationSchema}
                onSubmit={(values, {setSubmitting, resetForm}) => {
                    setSubmitting(true);
                    resetForm();
                    setUserInfo(userData.id, values);
                    setSubmitting(false);
                    getUserData();
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
                            <label htmlFor="age" className="form-label">Wiek</label>
                            <input
                                type="text"
                                name="age"
                                placeholder={`${userData.age == null ? "Wiek" : userData.age}`}
                                id="age"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.age}
                                className={`${touched.age && errors.age ? 'error' : null} form-control`}
                            />
                            {touched.age && errors.age ? (
                            <div className="error-message">{errors.age}</div>
                            ): null}
                        </div>
                        <div className='mb-3'>
                            <label htmlFor="height" className="form-label">Wzrost</label>
                            <input
                                type="text"
                                name="height"
                                placeholder={`${userData.height == null ? "Wzrost" : userData.height}`}
                                id="height"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.height}
                                className={`${touched.height && errors.height ? 'error' : null} form-control`}
                            />
                            {touched.height && errors.height ? (
                            <div className="error-message">{errors.height}</div>
                            ): null}
                        </div>
                        <div className='mb-3'>
                            <label htmlFor="weight" className="form-label">Waga</label>
                            <input
                                type="text"
                                name="weight"
                                placeholder={`${userData.weight == null ? "Waga" : userData.weight}`}
                                id="weight"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.weight}
                                className={`form-control ${touched.weight && errors.weight ? "error" : null}`}
                            />
                            {touched.weight && errors.weight ? (
                            <div className="error-message">{errors.weight}</div>
                            ): null}
                        </div>
                        <div className='mb-3'>
                            <label htmlFor="experience" className="form-label">Poziom doświadczenia</label>
                            <select
                                name="experience"
                                id="experience"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.experience}
                                className={`form-select ${touched.experience && errors.experience ? "error" : null}`}>
                                    <option value={''} selected disabled>Wybierz poziom zaawansowania</option>
                                    <option value={'B'} >Początkujący</option>
                                    <option value={'I'} >Średniozaawansowany</option>
                                    <option value={'A'} >Zaawansowany</option>
                            </select>
                            {touched.experience && errors.experience ? (
                            <div className="error-message">{errors.experience}</div>
                            ): null}
                        </div>
                        <button className="btn btn-primary" type="submit" disabled={isSubmitting}>Zatwierdź</button>
                    </form>
                )}
                </Formik>
                </div>
            </div>
        </div>
    )

}

export default UserPage