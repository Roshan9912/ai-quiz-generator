const BASE_URL = "https://reimagined-goldfish-7vpq45p4rqp6fxwwr-8000.app.github.dev";

export async function generateQuiz(url) {
  const res = await fetch(BASE_URL + "/generate_quiz", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });
  if (!res.ok) {
    let message = "Generation failed";
    try { message = (await res.json()).detail || message } catch {}
    throw new Error(message);
  }
  return await res.json();
}

export async function getHistory() {
  const res = await fetch(BASE_URL + "/history");
  return res.json();
}
export async function getQuiz(quizId) {
  const res = await fetch(BASE_URL + `/quiz/${quizId}`);
  return res.json();
}
