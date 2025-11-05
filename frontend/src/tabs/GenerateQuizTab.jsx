import React, { useState } from "react"
import { generateQuiz } from "../services/api"
import QuizDisplay from "../components/QuizDisplay"
export default function GenerateQuizTab() {
  const [url, setUrl] = useState("")
  const [loading, setLoading] = useState(false)
  const [quiz, setQuiz] = useState(null)
  const [error, setError] = useState("")
  const handleSubmit = async e => {
    e.preventDefault(); setError("")
    if (!/wikipedia\.org\/wiki/.test(url)) return setError("Enter a valid Wikipedia article URL")
    setLoading(true)
    try { setQuiz(await generateQuiz(url)) }
    catch { setError("Failed to generate quiz") }
    setLoading(false)
  }
  return (
    <div>
      <form onSubmit={handleSubmit} className="flex gap-2 mb-3">
        <input value={url} onChange={e=>setUrl(e.target.value)} className="border p-2 flex-1" placeholder="Wikipedia URL" />
        <button className="btn" type="submit">Generate Quiz</button>
      </form>
      {loading && <div>Loading...</div>}
      {error && <div className="text-red-700">{error}</div>}
      {quiz && <QuizDisplay quiz={quiz} />}
    </div>
  )
}
