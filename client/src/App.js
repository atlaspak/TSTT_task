import React, { useState, useEffect } from 'react';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('/api/items')
      .then(response => response.json())
      .then(setItems)
      .catch(error => console.error('Error:', error));
  }, []);
  
  return (
    <div>
      <h1>Test Results</h1>
      <table>
        <thead>
          <tr>
            <th>Platform</th>
            <th>Type</th>
            <th>Test-Scenario</th>
            <th>Configuration</th>
            <th>Results</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={index}>
              <td>{item.platform}</td>
              <td>{item.type}</td>
              <td>{item.scenario}</td>
              <td>{item.config}</td>
              <td>{item.steps.map(step => step.result.toUpperCase()).join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;