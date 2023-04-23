import { createContext, useState, useEffect } from "react";
import jwt_decode from 'jwt-decode';
import { useNavigate } from 'react-router-dom'

const AuthContext = createContext()

export default AuthContext;

export const AuthProvider = ({children}) => {


    let [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null)
    let [loading, setLoading] = useState(true)

    const naviagte = useNavigate()      

    let loginUser = async (values) => {
        let response = await fetch('http://localhost:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({'username':values.username, 'password': values.password})
        })

        let data = await response.json()

        if(response.status === 200){
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            naviagte('')
        }else{
            alert('Something went wrong')
        }
    }

    let logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        naviagte('/login')
    }

    let registerUser = async (values) => {
        let respone = await fetch('http://localhost:8000/api/register/', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                'username': values.username,
                'email': values.email,
                'password': values.password
            })
        })

        if(respone.status === 201){
            naviagte('/login');
        }else{
            alert('Something went wrong')
        }
    }

    let setUserInfo = async(id, values) => {
        let respone = await fetch(`http://localhost:8000/api/user/${id}/`, {
            method: 'PUT',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                'id': id,
                'age': values.age,
                'height': values.height,
                'weight': values.weight,
                'experience': values.experience,
            })
        })

        if(respone.status === 400){
            alert('Failed to change data')
        }
    }

    let updateToken = async () => {
        let response = await fetch('http://localhost:8000/api/token/refresh/', {
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({'refresh':authTokens.refresh})
        })
        let data = await response.json()

        if(response.status === 200){
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
        }else{
            logoutUser()
        }
    }

    let contextData = {
        user:user,
        loginUser:loginUser,
        logoutUser:logoutUser,
        registerUser:registerUser,
        setUserInfo:setUserInfo,
        authTokens:authTokens
    }

    useEffect(() => {
        let fourMinutes = 1000 * 60 * 4;
        let interval = setInterval( () => {
            if(authTokens){
                updateToken()
            }
        }, fourMinutes)
        return () => clearInterval(interval )

    }, [authTokens, loading])

    return (
        <AuthContext.Provider value={contextData }>
            {children}
        </AuthContext.Provider>
    )
}