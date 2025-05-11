async function sendData() {
  const input = document.getElementById('inputValue').value;
  const response = await fetch('/calculate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({input})
  });
  const data = await response.json();
  document.getElementById('result').innerText = data.result;
}
