import {React, useState, useEffect, useContext} from "react";
import AuthContext from "../context/AuthContext";
import {useParams} from 'react-router-dom'

const UserGymPage = () => {

    let [allEquipments, getAllEquipments] = useState([]);
    let {authTokens, user} = useContext(AuthContext)

    const params = useParams();

    useEffect(() => {
        getEquipments()
    }, [])

    let getEquipments = async() => {
        let response = await fetch('http://localhost:8000/api/user/gyms/equipments/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        let data = await response.json()
        getAllEquipments(data)
    }

    return (
        <div>{params.id}</div>
    )
}


export default UserGymPage