import {React, useState, useEffect, useContext} from "react";
import AuthContext from "../context/AuthContext";
import { useNavigate, NavLink } from 'react-router-dom';
import { Formik } from 'formik';
import * as Yup from 'yup';
import '../styles/forms.css';

const yesterday = new Date(Date.now() -86400000);
const validationSchema = Yup.object().shape({
    muscle: Yup.number()
    .required("Partia mięśni jest wymagana."),
    gym: Yup.number()
    .required("Siłownia jest wymagana."),
    date: Yup.date()
    .required("Data jest wymagana.")
    .min(yesterday, "Data nie moze być w przeszłości.")
  });

const UserWorkoutListPage = () => {
    let [userWorkouts, setUserWorkouts] = useState([]);
    let [userPastWorkouts, setPastUserWorkouts] = useState([]);
    let {authTokens} = useContext(AuthContext)
    let [muscles, setMuscles] = useState([]);
    let [userGyms, setUserGyms] = useState([]);

    useEffect(() => {
        getUserWorkoutData()
        getMuscles()
        getUserGymsData()
    }, [])

    let getUserWorkoutData = async() => {
        let response = await fetch('http://localhost:8000/api/user/workouts/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        let currentDate = new Date();

        let filteredData = data.filter(item => new Date(item.date) >= currentDate);
        let filteredPastData = data.filter(item => new Date(item.date) < currentDate);
        
        filteredData.sort((a, b) => (new Date(a.date) > new Date(b.date)) ? 1 : ((new Date(b.date) > new Date(a.date)) ? -1 : 0));
        filteredPastData.sort((a, b) => (new Date(a.date) > new Date(b.date)) ? 1 : ((new Date(b.date) > new Date(a.date)) ? -1 : 0));

        setUserWorkouts(filteredData);
        setPastUserWorkouts(filteredPastData);
        
    }

    let getMuscles = async () => {
        let response = await fetch('http://127.0.0.1:8000/api/muscles/')
        let data = await response.json()
        setMuscles(data)

    }

    let getUserGymsData = async() => {
        let response = await fetch('http://localhost:8000/api/user/gyms/all/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        setUserGyms(data)
    }

    let createWorkout = async(values) => {
        let response = await fetch(`http://localhost:8000/api/user/workouts/create/`,{
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                'Authorization': 'Bearer ' + String(authTokens.access)
            },
            body: JSON.stringify({
                'muscle_id': values.muscle,
                'gym_id': values.gym,
                'date': values.date
            })
        })
        let data = await response.json()
        alert(data);
    }

    return (
        <div className="container-fluid mt-3">
            <div className="row">
                <div className="col-12 col-md-6 text-center">
                    <p className="h1">Twoje zaplanowane treningi</p>
                    <div className="row">
                    {userWorkouts.map((workout, index) => (
                    <div key={index} className="text-center col-12 col-sm-6 col-md-4 my-2 py-3 bg-light border">
                        <NavLink to={'/workouts/'+workout.id} className="nav-link">
                        <p className="h2">{workout.muscle}</p>
                        <p className="h4">{workout.gym}</p>
                        <p>{workout.date}</p>
                        </NavLink>
                    </div>
                    ))}
                    </div>
                </div>

                <div className="col-12 col-md-6">
                <p className="h1 text-center">Zaplanuj nowy trening</p>
                    <Formik
                    initialValues={{muscle: "", gym: "", date: ""}}
                    validationSchema={validationSchema}
                    onSubmit={(values, {setSubmitting, resetForm}) => {
                        setSubmitting(true);
                        resetForm();
                        createWorkout(values)
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
                                <label htmlFor="muscle" className="form-label">Partia mięśniowa</label>
                                <select
                                    name="muscle"
                                    id="muscle"
                                    onChange={handleChange}
                                    onBlur={handleBlur}
                                    className={`form-select ${touched.muscle && errors.muscle ? "error" : null}`}>
                                        <option disabled selected>Wybierz partie</option>
                                        {muscles.map((muscle, index) => (
                                        <option key={index} value={muscle.id}>{muscle.muscle_name}</option>
                                        ))}
                                </select>
                                {touched.muscle && errors.muscle ? (
                                <div className="error-message">{errors.muscle}</div>
                                ): null}
                            </div>
                            <div className='mb-3'>
                                <label htmlFor="gym" className="form-label">Siłownia</label>
                                <select
                                    name="gym"
                                    id="gym"
                                    onChange={handleChange}
                                    onBlur={handleBlur}
                                    className={`form-select ${touched.gym && errors.gym ? "error" : null}`}>
                                        <option disabled selected>Wybierz siłownie</option>
                                        {userGyms.map((gym, index) => (
                                        <option key={index} value={gym.id}>{gym.gym_name}</option>
                                        ))}
                                </select>
                                {touched.gym && errors.gym ? (
                                <div className="error-message">{errors.gym}</div>
                                ): null}
                            </div>
                            <div className='mb-3'>
                                <label htmlFor="date" className="form-label">Data</label>
                                <input
                                    type="date"
                                    name="date"
                                    id="date"
                                    onChange={handleChange}
                                    onBlur={handleBlur}
                                    className={`${touched.date && errors.date ? 'error' : null} form-control`}
                                />
                                {touched.date && errors.date ? (
                                <div className="error-message">{errors.date}</div>
                                ): null}
                            </div>
                            <button className="btn btn-primary" type="submit" disabled={isSubmitting}>Dodaj</button>
                        </form>
                    )}
                    </Formik>
                </div>
            </div>
            <div className="col-12 col-md-6 text-center">
                <p className="h1">Odbyte treningi</p>
                <div className="row">
                    {userPastWorkouts.map((workout, index) => (
                    <div key={index} className="text-center col-12 col-sm-6 col-md-4 my-2 py-3 bg-light border">
                        <NavLink to={'/workouts/'+workout.id+'/done/'} className="nav-link">
                        <p className="h2">{workout.muscle}</p>
                        <p className="h4">{workout.gym}</p>
                        <p>{workout.date}</p>
                        </NavLink>
                    </div>
                    ))}
                    </div>
            </div>
        </div>
    )

}

export default UserWorkoutListPage