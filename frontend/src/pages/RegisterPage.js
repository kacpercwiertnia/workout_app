import {React, useContext} from 'react';
import { Formik } from 'formik';
import * as Yup from 'yup';
import '../styles/forms.css';
import AuthContext from '../context/AuthContext';

const passwordRegExp = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!_%*?&]{8,}$/

const validationSchema = Yup.object().shape({
    username: Yup.string()
    .max(100, "Nazwa użytkownika nie może być dłuższa niż 100 znaków.")
    .required("Nazwa użytkownika jest wymagana."),
    email: Yup.string()
    .email("Adres Email musi być poprawny, np: nazwa@domena.pl.")
    .max(100, "Adres Email nie może być dłuższy niz 100 znaków.")
    .required("Adres Email jest wymagany."),
    password: Yup.string()
    .required("Hasło jest wymagane.")
    .matches(passwordRegExp, "Hasło musi mieć co najmniej 8 znaków, w tym jedną wielką literę, jedną małą literę, jeden znak specjalny i jedną cyfrę."),
    password2: Yup.string()
    .required("Potwierdzenie hasła jest wymagane.")
    .oneOf([Yup.ref('password'), null], "Hasła muszą myć takie same.")
  });

const RegitserPage = () => { 
    let {registerUser} = useContext(AuthContext)
    return (
        <div className='container mt-3'>
            <div className='row justify-content-center'>
                <div className='col-12 col-sm-8 col-md-6'>
                <Formik
                initialValues={{username: "", email: "", password: "", password2: ""}}
                validationSchema={validationSchema}
                onSubmit={(values, {setSubmitting, resetForm}) => {
                    setSubmitting(true);
                    resetForm();
                    registerUser(values);
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
                            <label htmlFor="username" className="form-label">Nazwa użytkownika</label>
                            <input
                                type="text"
                                name="username"
                                placeholder="Nazwa użytkownika"
                                id="username"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.username}
                                className={`${touched.username && errors.username ? 'error' : null} form-control`}
                            />
                            {touched.username && errors.username ? (
                            <div className="error-message">{errors.username}</div>
                            ): null}
                        </div>
                        <div className='mb-3'>
                            <label htmlFor="email" className="form-label">Adres Email</label>
                            <input
                                type="text"
                                name="email"
                                placeholder="Adres Email"
                                id="email"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.email}
                                className={`${touched.email && errors.email ? 'error' : null} form-control`}
                            />
                            {touched.email && errors.email ? (
                            <div className="error-message">{errors.email}</div>
                            ): null}
                        </div>
                        <div className='mb-3'>
                            <label htmlFor="password" className="form-label">Hasło</label>
                            <input
                                type="password"
                                name="password"
                                placeholder="Hasło"
                                id="password"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.password}
                                className={`form-control ${touched.password && errors.password ? "error" : null}`}
                            />
                            {touched.password && errors.password ? (
                            <div className="error-message">{errors.password}</div>
                            ): null}
                        </div>
                        <div className='mb-3'>
                            <label htmlFor="password2" className="form-label">Powtórz Hasło</label>
                            <input
                                type="password"
                                name="password2"
                                placeholder="Hasło"
                                id="password2"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.password2}
                                className={`form-control ${touched.password2 && errors.password2 ? "error" : null}`}
                            />
                            {touched.password2 && errors.password2 ? (
                            <div className="error-message">{errors.password2}</div>
                            ): null}
                        </div>
                        <button className="btn btn-primary" type="submit" disabled={isSubmitting}>Zarejestruj się</button>
                    </form>
                )}
                </Formik>
                </div>
            </div>
        </div>
    );
};

export default RegitserPage;