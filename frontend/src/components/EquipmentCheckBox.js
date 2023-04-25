import React, { useState, useEffect } from 'react';

const EquipmentCheckBox = ({eq, index, initial, ...props}) => {
    const [checked, setChecked] = useState(initial);

    useEffect(() => {
        setChecked(initial);
    }, [initial]);

    return (
        <div className ="form-check form-check-inline">
            <input className="form-check-input" checked={checked} onChange={() => {
                setChecked(prev => !prev);
            }} type="checkbox" id={index} value={eq.id}/>
            <label className="form-check-label" htmlFor={index}>{eq.equipment_name}</label>
        </div>
    )
};

export default EquipmentCheckBox;