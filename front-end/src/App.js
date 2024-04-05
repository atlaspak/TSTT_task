import React, { useState, useEffect } from 'react';
import Summary from './Summary';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('/api/items')
      .then(response => response.json())
      .then(setItems)
      .catch(error => console.error('Error:', error));
  }, []);

  const getOverallResult = (steps) => {
    const results = steps.map(step => step.result);
    if (results.includes('fail')) return 'FAIL';
    if (results.includes('busy') || results.includes('wait')) return 'UNSTABLE';
    return 'PASS';
  };

  return (
    <div>
      <Summary/>
      <h1>Test Results</h1>
      <table>
        <thead>
          <tr>
            <th>Platform</th>
            <th>Type</th>
            <th>Test-Scenario</th>
            <th>Configuration</th>
            <th>Results</th>
            <th>Overall</th>
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
              <td>{getOverallResult(item.steps)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;