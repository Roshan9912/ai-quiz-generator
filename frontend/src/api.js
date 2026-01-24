const API_BASE = "http://localhost:8000";

export async function generateQuiz(wikiUrl) {
  const response = await fetch(`${API_BASE}/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url: wikiUrl }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text);
  }

  return response.json();
}

export async function getHistory() {
  const response = await fetch(`${API_BASE}/history`);
  return response.json();
}
