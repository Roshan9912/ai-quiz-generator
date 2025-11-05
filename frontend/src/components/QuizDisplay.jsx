export default function QuizDisplay({ quiz }) {
  if (!quiz) return null
  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="font-bold text-xl mb-3">{quiz.summary}</h2>
      <div className="mb-3 text-xs text-gray-400">Entities: {Object.entries(quiz.key_entities||{})
        .map(([k,v])=>`${k}: ${v.join(", ")}`).join(" | ")}</div>
      <div className="mb-3">Sections: {quiz.sections && quiz.sections.join(", ")}</div>
      <div className="mb-3">Related topics: {quiz.related_topics && quiz.related_topics.join(", ")}</div>
      <ul className="divide-y">
        {quiz.quiz.map((q,i)=>(
          <li key={i} className="py-3">
            <b>Q{i+1}: {q.question}</b>
            <ol className="ml-6">{q.options.map((opt,j)=><li key={j}>{opt}</li>)}</ol>
            <div>Answer: {q.answer}</div>
            <div>Difficulty: {q.difficulty}</div>
            <div className="text-green-600">Explanation: {q.explanation}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
