import React, { useState, useEffect } from 'react';

const ShareGymCheckBox = ({gymid, initial, ...props}) => {
    const [checked, setChecked] = useState(initial);

    useEffect(() => {
        setChecked(initial);
    }, [initial]);

    let shareGym = async () => {
        const response = await fetch(`http://localhost:8000/api/user/gyms/${gymid}/share/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({is_shared: !checked})
        });
        
        if (response.status === 400) {
          alert('Failed to change data');
        }
    }

    return (
        <div className ="form-check form-check-inline">
            <input className="form-check-input" checked={checked} onChange={() => {
                setChecked(prev => !prev);
                shareGym()
            }} type="checkbox" id={gymid} value={gymid}/>
            <label className="form-check-label" htmlFor={gymid}>Udostępnij siłownie</label>
        </div>
    )
};

export default ShareGymCheckBox;