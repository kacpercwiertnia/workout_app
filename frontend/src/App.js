import React from 'react';
import MusclesListPage from './pages/MusclesListPage';
import NavbarComponent from './components/Navbar';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AuthRoute from './utils/AuthRoute';
import UnauthRoute from './utils/UnauthRoute';
import { AuthProvider } from './context/AuthContext'
import UserPage from './pages/UserPage';

function App() {
  return (
    <Router>
      <AuthProvider>
        <NavbarComponent/>
        <Routes>
          <Route path='/' exact element={<HomePage/>}/>
          <Route path='/muscles' element={<AuthRoute/>}>
            <Route path='/muscles' element={<MusclesListPage/>}/>
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
