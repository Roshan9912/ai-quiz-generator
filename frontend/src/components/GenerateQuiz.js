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
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Wikipedia URL"
      />

      <button onClick={submit}>
        {loading ? "Generating..." : "Generate Quiz"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && data.quiz && data.quiz.map((q, i) => (
        <div key={i} className="card">
          <h4>{q.question}</h4>
          <ul>
            {q.options.map((opt, idx) => (
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
