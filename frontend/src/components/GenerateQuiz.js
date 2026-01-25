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

      console.log("API RESULT:", result);

      // 🔑 Normalize quiz safely
      let quiz = [];

      if (Array.isArray(result.quiz)) {
        quiz = result.quiz;
      } else if (typeof result.quiz === "string") {
        try {
          quiz = JSON.parse(result.quiz);
        } catch {
          quiz = [];
        }
      } else if (result.quiz?.quiz && Array.isArray(result.quiz.quiz)) {
        quiz = result.quiz.quiz;
      }

      setData({ ...result, quiz });

    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Wiki Quiz Generator</h2>

      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Wikipedia URL"
        style={{ width: "60%", padding: "8px" }}
      />

      <br /><br />

      <button onClick={submit} disabled={loading}>
        {loading ? "Generating..." : "Generate Quiz"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data?.quiz?.length > 0 &&
        data.quiz.map((q, i) => (
          <div key={i} className="card" style={{
            border: "1px solid #ccc",
            marginTop: "20px",
            padding: "15px"
          }}>
            <h4>{q.question}</h4>
            <ul>
              {Array.isArray(q.options) &&
                q.options.map((opt, idx) => (
                  <li key={idx}>{opt}</li>
                ))}
            </ul>
            <p><b>Answer:</b> {q.answer}</p>
            <p><b>Difficulty:</b> {q.difficulty}</p>
            <p>{q.explanation}</p>
          </div>
        ))}
    </div>
  );
}

export default GenerateQuiz;
