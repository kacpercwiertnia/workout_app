import {React, useState, useEffect, useContext} from "react";
import AuthContext from "../context/AuthContext";
import {useParams} from 'react-router-dom';

const UserWorkoutPage = () => {

    let [userWorkout, setUserWorkout] = useState([]);
    let [userExercises, setUserExercises] = useState([]);
    let {authTokens, user} = useContext(AuthContext)

    const params = useParams();

    useEffect(() => {
        getWorkout()
    },[])


    let getWorkout = async() => {
        let response = await fetch(`http://localhost:8000/api/user/workouts/${params.id}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        setUserWorkout(data)
        console.log(data)
        let i = 0;
        let tmp = []
        for(const el of data){
            if(i != 0){
                tmp.push(el);
            }
            i++;
        }
        console.log(tmp)
        setUserExercises(tmp)
    }

    return (
        <div>
            <div className="container-fluid">
                <div className="row justify-content-center">
                    <div className="col-12 text-center mt-2">
                        <p className="h1">Trening:</p>
                        <p className="h3">{userWorkout[0]?.muscle} {userWorkout[0]?.gym} {userWorkout[0]?.date}</p>
                        <p className="h2">Ćwiczenia:</p>
                        <table class="table table-striped">
                        <thead>
                            <tr>
                            <th></th>
                            <th scope="col">#</th>
                            <th scope="col">Nazwa</th>
                            <th scope="col">Przyrząd</th>
                            <th scope="col">Opis</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                               userExercises.map((el, index) => (
                                
                                <tr key={index}>
                                <button class="btn btn-outline-danger btn-block btn-sm">x</button>
                                <td>{index+1}</td>
                                <td>{el?.exercise_name}</td>
                                <td>{el?.equipment}</td>
                                <td>{el?.description}</td>
                                </tr>
                            ))  
                            }
                        </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default UserWorkoutPage;

//                        <p className="h3">{userWorkout[0].muscle} {userWorkout[0].gym} {userWorkout[0].date}</p>
//userExercises.map((el, index) => (
//    <p className="h3" key={index}>{el.exercise_name} {el.equipment} {el.description}</p>
//    ))