import React from 'react';
import { useAuthContext } from "@asgardeo/auth-react";

const clients = [
  { firstName: 'John', lastName: 'Doe', company: 'Company A' },
  { firstName: 'Jane', lastName: 'Smith', company: 'Company B' },
  { firstName: 'Michael', lastName: 'Johnson', company: 'Company C' },
];

const ClientListPage = () => {
  const { signOut } = useAuthContext();

  return (
    <div>
      <h1>Client List</h1>
      <button onClick={() => signOut()}>Logout</button>
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Company</th>
          </tr>
        </thead>
        <tbody>
          {clients.map((client, index) => (
            <tr key={index}>
              <td>{client.firstName}</td>
              <td>{client.lastName}</td>
              <td>{client.company}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ClientListPage;
