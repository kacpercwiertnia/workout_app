import {React, useContext} from 'react';
import { Formik } from 'formik';
import * as Yup from 'yup';
import '../styles/forms.css';
import AuthContext from '../context/AuthContext';

const validationSchema = Yup.object().shape({
    username: Yup.string()
    .max(100, "Nazwa użytkownika nie może być dłuższa niż 100 znaków.")
    .required("Nazwa użytkownika jest wymagana."),
    password: Yup.string()
    .required("Hasło jest wymagane.")
  });

const LoginPage = () => {
    let {loginUser} = useContext(AuthContext)
    return (
        <div className='container mt-3'>
            <div className='row justify-content-center'>
                <div className='col-12 col-sm-8 col-md-6'>
                <Formik
                initialValues={{username: "", password: ""}}
                validationSchema={validationSchema}
                onSubmit={(values, {setSubmitting, resetForm}) => {
                    setSubmitting(true);
                    resetForm();
                    loginUser(values);
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
                        <button className="btn btn-primary" type="submit" disabled={isSubmitting}>Zaloguj się</button>
                    </form>
                )}
                </Formik>
                </div>
            </div>
        </div>
    );
};

export default LoginPage;