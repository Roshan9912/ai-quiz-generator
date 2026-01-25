const API_BASE = "https://ai-quiz-generator-1-6jbj.onrender.com";

export async function generateQuiz(url) {
  const res = await fetch(`${API_BASE}/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url }),
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || "Failed to generate quiz");
  }

  return res.json();
}

export async function getHistory() {
  const res = await fetch(`${API_BASE}/history`);
  if (!res.ok) {
    throw new Error("Failed to fetch history");
  }
  return res.json();
}
