import {React, useState, useEffect, useContext} from "react";
import AuthContext from "../context/AuthContext";
import {useParams} from 'react-router-dom';
import { Formik } from 'formik';
import * as Yup from 'yup';
import '../styles/forms.css';
import EquipmentCheckBox from "../components/EquipmentCheckBox";

const UserGymPage = () => {

    let [allEquipments, getAllEquipments] = useState([]);
    let [gymEquipments, setGymEquipments] = useState([]);
    let [userGym, setUserGym] = useState([]);
    let {authTokens, user} = useContext(AuthContext)

    const params = useParams();

    useEffect(() => {
        getEquipments()
        getUserGymData()
        getGymEquipments()
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

    let getGymEquipments = async() => {
        let response = await fetch(`http://localhost:8000/api/user/gyms/${params.id}/equipments/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        setGymEquipments(data)
    }

    let getUserGymData = async() => {
        let response = await fetch(`http://localhost:8000/api/user/gyms/${params.id}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        setUserGym(data)
    }

    let setGymInfo = async(data) => {
        let respone = await fetch(`http://localhost:8000/api/user/gyms/${params.id}/update/`, {
            method: 'PUT',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })

        if(respone.status === 400){
            alert('Failed to change data')
        }
    }

    let handleSubmit = (event) => {
        event.preventDefault();
        let updated_gym_equipment = []
        for(const el of event.target){
            updated_gym_equipment.push({equipment_id: el.value, is_checked: el.checked})
        }
        updated_gym_equipment.pop()
        setGymInfo(updated_gym_equipment);
    }

    return (
        <div className="container-fluid">
            <div className="row mt-3 justify-content-center">
                <div className="col-12 text-center">
                    <p className="h1">{userGym.gym_name}</p>
                    <p className="h5">{userGym.address}</p>
                    <p className="h4">Sprzęt dostępny na tej siłwoni:</p>
                </div>
                <div className="col-8 text-center mt-2">
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                        {allEquipments.map((eq, index) => {
                            let found = false;
                            for( const el of gymEquipments){
                                if(el.equipment_id === eq.id){
                                    found = true;
                                    break;
                                }}
                                return (
                                    <EquipmentCheckBox
                                        eq={eq}
                                        key={index}
                                        initial={found}
                                    />
                                )
                            })}
                        </div>
                        <button className="btn btn-primary" type="submit">Ustaw</button>
                    </form>
                </div>
            </div>
        </div>
    )
}


export default UserGymPage