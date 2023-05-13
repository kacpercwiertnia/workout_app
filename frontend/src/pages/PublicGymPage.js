import {React, useState, useEffect, useContext} from "react";
import AuthContext from "../context/AuthContext";
import {useParams} from 'react-router-dom';
import { Formik } from 'formik';
import * as Yup from 'yup';
import '../styles/forms.css';
import EquipmentCheckBox from "../components/EquipmentCheckBox";
import AddGymCheckBox from "../components/AddGymCheckBox";

const PublicGymPage = () => {

  let [gymPublicEquipments, setPublicGymEquipments] = useState([]);
  let [isGymAdded, setGymAddedState] = useState(null);
  let {authTokens, user} = useContext(AuthContext)

  const params = useParams();

  useEffect(() => {
    getPublicGymEquipments()
    checkIfGymAdded()
  }, [])

  let getPublicGymEquipments = async() => {
    let response = await fetch(`http://localhost:8000/api/user/gyms/sharedlist/${params.id}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + String(authTokens.access)
        }
    })
    let data = await response.json()
    setPublicGymEquipments(data)
  }

  let checkIfGymAdded = async() => {
    let response = await fetch(`http://localhost:8000/api/user/gyms/sharedlist/${params.id}/isAdded/`,{
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + String(authTokens.access)
      }
    })
    let data = await response.json()
    setGymAddedState(data);
  }


  return (
    <div className="col-12 col-md-12">
      <p className="h2 text-center">Sprzęt dostępny na siłowni</p>
      <div className="row">
        {gymPublicEquipments.map((equipment, index) => (
          <div key={index} className="col-12 col-sm-6 col-md-4 text-center">
            <p className="h6">{equipment.eq_name}</p>
          </div>
        ))}
        <div className="mb-3 text-center">
          <AddGymCheckBox
            gymid={params.id}
            initial={isGymAdded}
          />
        </div>
      </div>
    </div>
  )
}


export default PublicGymPage
