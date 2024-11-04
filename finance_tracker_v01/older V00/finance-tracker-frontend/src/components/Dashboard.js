import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Dashboard() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://localhost:8080/api/transactions/', {
          headers: {
            'Authorization': `Bearer ${token}` // Corrected here
          }
        });
        setTransactions(response.data);
      } catch (error) {
        console.error('Error fetching transactions', error);
      }
    };
    fetchTransactions();
  }, []);

  return (
    <div>
      <h1>Your Transactions</h1>
      <ul>
        {transactions.map((transaction) => (
          <li key={transaction.id}>
            {transaction.amount} - {transaction.category}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
