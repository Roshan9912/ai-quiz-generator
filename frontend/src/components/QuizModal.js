export default function QuizModal({ data, onClose }) {
  return (
    <div style={{ background: "#eee", padding: 20 }}>
      <button onClick={onClose}>Close</button>
      <h3>{data.title}</h3>

      {data.quiz.map((q, i) => (
        <div key={i}>
          <b>{q.question}</b>
          <p>Answer: {q.answer}</p>
        </div>
      ))}
    </div>
  );
}
