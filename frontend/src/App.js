import React from 'react';
import NavbarComponent from './components/Navbar';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import { BrowserRouter as Router, Routes, Route, useParams } from 'react-router-dom';
import AuthRoute from './utils/AuthRoute';
import UnauthRoute from './utils/UnauthRoute';
import { AuthProvider } from './context/AuthContext'
import UserPage from './pages/UserPage';
import UserGymListPage from './pages/UserGymListPage';
import UserWorkoutListPage from './pages/UserWorkoutListPage';
import UserGymPage from './pages/UserGymPage';

function App() {
  return (
    <Router>
      <AuthProvider>
        <NavbarComponent/>
        <Routes>
          <Route path='/' exact element={<HomePage/>}/>
          <Route path='/gyms' element={<AuthRoute/>}>
            <Route path='/gyms' element={<UserGymListPage/>}/>
          </Route>
          <Route path='/gyms/:id' element={<AuthRoute/>}>
            <Route path='/gyms/:id' element={<UserGymPage />}/>
          </Route>
          <Route path='/workouts' element={<AuthRoute/>}>
            <Route path='/workouts' element={<UserWorkoutListPage/>}/>
          </Route>
          <Route path='/login' element={<UnauthRoute/>}>
            <Route path='/login' element={<LoginPage/>}/>
          </Route>
          <Route path='/register' element={<UnauthRoute/>}>
            <Route path='/register' element={<RegisterPage/>}/>
          </Route>
          <Route path='/user' element={<AuthRoute/>}>
            <Route path='/user' element={<UserPage/>}/>
          </Route>
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
