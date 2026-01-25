import { generateQuiz } from "../api";
import { useState } from "react";

function GenerateQuiz() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const submit = async () => {
    try {
      setLoading(true);
      setError("");
      const result = await generateQuiz(url);
      console.log("API RESULT:", result); // 🔍 DEBUG
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // ✅ HARD NORMALIZATION (NO MORE ERRORS)
  let quizArray = [];

  if (data?.quiz) {
    if (Array.isArray(data.quiz)) {
      quizArray = data.quiz;
    } else if (typeof data.quiz === "string") {
      try {
        quizArray = JSON.parse(data.quiz);
      } catch {
        quizArray = [];
      }
    } else if (typeof data.quiz === "object" && Array.isArray(data.quiz.quiz)) {
      quizArray = data.quiz.quiz;
    }
  }

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "auto" }}>
      <h2>AI Wiki Quiz Generator</h2>

      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Wikipedia URL"
        style={{ width: "100%", padding: "8px" }}
      />

      <button onClick={submit} disabled={loading}>
        {loading ? "Generating..." : "Generate Quiz"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {quizArray.length > 0 && (
        <div style={{ marginTop: "20px" }}>
          <h3>{data.title}</h3>
          <p>{data.summary}</p>

          {quizArray.map((q, i) => (
            <div
              key={i}
              style={{
                border: "1px solid #ccc",
                padding: "15px",
                marginBottom: "10px",
                borderRadius: "6px",
              }}
            >
              <h4>{i + 1}. {q.question}</h4>
              <ul>
                {q.options?.map((opt, idx) => (
                  <li key={idx}>{opt}</li>
                ))}
              </ul>
              <p><b>Answer:</b> {q.answer}</p>
              <p><b>Difficulty:</b> {q.difficulty}</p>
              <p>{q.explanation}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default GenerateQuiz;
