import { Outlet, Navigate } from 'react-router-dom'
import { useContext } from 'react'
import AuthContext from '../context/AuthContext'

const FormRoute = () => {
    let {user, getFormUserData} = useContext(AuthContext)

    return (
        (user && getFormUserData) ? <Outlet/> : <Navigate to='/login'/>
    )
}

export default FormRoute