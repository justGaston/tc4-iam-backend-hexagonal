import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './LoginPage';
import ClientListPage from './ClientListPage';
import { useAuthContext } from "@asgardeo/auth-react";

const App = () => {
  const { state } = useAuthContext();

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        {state.isAuthenticated && <Route path="/clients" element={<ClientListPage />} />}
        <Route path="/callback" element={<LoginPage />} />
      </Routes>
    </Router>
  );
};

export default App;
