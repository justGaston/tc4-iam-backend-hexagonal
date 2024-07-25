import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { AuthProvider } from "@asgardeo/auth-react";
import config from './config';

ReactDOM.render(
  <AuthProvider config={config}>
    <App />
  </AuthProvider>,
  document.getElementById('root')
);
