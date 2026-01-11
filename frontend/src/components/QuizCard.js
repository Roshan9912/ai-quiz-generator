export default function QuizCard({ data }) {
  // Handle backend error responses safely
  if (!data || data.detail) {
    return (
      <div style={{ color: "red" }}>
        <h4>Error</h4>
        <p>{data?.detail || "Something went wrong"}</p>
      </div>
    );
  }

  const sections = Array.isArray(data.sections) ? data.sections : [];
  const quiz = Array.isArray(data.quiz) ? data.quiz : [];

  return (
    <div>
      <h3>{data.title}</h3>

      <h4>Sections</h4>
      {sections.length === 0 ? (
        <p>No sections available</p>
      ) : (
        <ul>
          {sections.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ul>
      )}

      <h4>Quiz</h4>
      {quiz.length === 0 ? (
        <p>No quiz questions available</p>
      ) : (
        quiz.map((q, i) => (
          <div
            key={i}
            style={{ border: "1px solid #ccc", margin: 10, padding: 10 }}
          >
            <b>{q.question}</b>
            <ul>
              {(q.options || []).map((o, j) => (
                <li key={j}>{o}</li>
              ))}
            </ul>
            <p><b>Answer:</b> {q.answer}</p>
            <p><i>{q.explanation}</i></p>
            <p>Difficulty: {q.difficulty}</p>
          </div>
        ))
      )}
    </div>
  );
}
