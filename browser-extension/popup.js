document.getElementById('summarizeBtn').addEventListener('click', () => {
  const inputText = document.getElementById('inputText').value.trim();
  const summaryDiv = document.getElementById('summaryResult');
  summaryDiv.textContent = "Summarizing...";

  if (!inputText) {
    summaryDiv.textContent = "Please enter some text to summarize.";
    return;
  }

  // Call Flask summarization API endpoint
  fetch('http://localhost:5000/summarize', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ inputtext: inputText })
  })
    .then(response => response.text())
    .then(html => {
      // Extract the summary text from the returned HTML (your Flask output.html)
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const summaryText = doc.querySelector('.summary-container')?.textContent || "No summary.";
      summaryDiv.textContent = summaryText;
    })
    .catch(error => {
      summaryDiv.textContent = "Error during summarization.";
      console.error(error);
    });
});
