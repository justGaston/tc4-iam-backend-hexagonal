import React, { useEffect } from 'react';
import { useAuthContext } from "@asgardeo/auth-react";
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
  const { state, signIn, signOut } = useAuthContext();
  const navigate = useNavigate();

  useEffect(() => {
    if (state.isAuthenticated) {
      navigate('/clients');
    }
  }, [state.isAuthenticated, navigate]);

  return (
    <div>
      <h1>Login Page</h1>
      {state.isAuthenticated ? (
        <button onClick={() => signOut()}>Logout</button>
      ) : (
        <button onClick={() => signIn()}>Login</button>
      )}
    </div>
  );
};

export default LoginPage;
