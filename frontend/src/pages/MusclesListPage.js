import React, {useState, useEffect} from "react";

const MusclesListPage = () => {

    let [muscles, setMuscles] = useState([]);

    useEffect(() => {
        getMuscles()
    }, [])

    let getMuscles = async () => {
        let response = await fetch('http://127.0.0.1:8000/api/muscles/')
        let data = await response.json()
        setMuscles(data)

    }

    return (
        <>
        <p className="h1 text-center"> List of Muscles </p>
        <div className="container-fluid">
            <div className="row justify-content-center mx-2">
            {muscles.map((muscle, index) => (
                <div key={index} className="text-center col-12 col-sm-6 col-md-4 my-2 py-3 bg-light border">{muscle.muscle_name}</div>
                ))}
            </div>
        </div>
        </>
    );
};

export default MusclesListPage;

/*
{muscles.map((muscle, index) => (
                <Col key={index} className="py-3 bg-light border">{muscle.muscle_name}</Col>
            ))}
*/