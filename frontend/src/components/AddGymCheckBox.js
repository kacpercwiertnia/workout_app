import React, { useState, useEffect, useContext } from 'react';
import AuthContext from "../context/AuthContext";

const AddGymCheckBox = ({gymid, initial, ...props}) => {
    const [checked, setChecked] = useState(initial);
    let {user} = useContext(AuthContext)

    useEffect(() => {
        setChecked(initial);
    }, [initial]);

    let addOrDeleteGym = async () => {
        const response = await fetch(`http://localhost:8000/api/user/gyms/sharedlist/${gymid}/addDelete/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({'action': !checked, 'user_id': user.user_id})
        });
        
        if (response.status === 400) {
          alert('Failed to change data');
        }
    }

    return (
        <div className ="form-check form-check-inline">
            <input className="form-check-input" checked={checked} onChange={() => {
                setChecked(prev => !prev);
                addOrDeleteGym()
            }} type="checkbox" id={gymid} value={gymid}/>
            <label className="form-check-label" htmlFor={gymid}>Dodaj siłownie jako moją</label>
        </div>
    )
};

export default AddGymCheckBox;