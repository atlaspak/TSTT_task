import React, { useState, useEffect } from 'react';

function Summary() {
  const [summary, setSummary] = useState({ total_scenarios: 0, statuses: {} });

  useEffect(() => {
    fetch('/api/summary')
      .then(response => response.json())
      .then(data => setSummary(data))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div>
      <h2>Summary</h2>
      <p>Total Scenarios: {summary.total_scenarios}</p>
      <p>Pass: {summary.statuses.pass}</p>
      <p>Fail: {summary.statuses.fail}</p>
      <p>Busy: {summary.statuses.busy}</p>
      <p>Wait: {summary.statuses.wait}</p>
    </div>
  );
}

export default Summary;
