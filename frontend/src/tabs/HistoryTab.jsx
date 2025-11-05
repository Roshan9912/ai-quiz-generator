import React, { useEffect, useState } from "react"
import { getHistory, getQuiz } from "../services/api"
import QuizDisplay from "../components/QuizDisplay"
import Modal from "../components/Modal"

export default function HistoryTab() {
  const [history, setHistory] = useState([])
  const [showModal, setShowModal] = useState(false)
  const [modalQuiz, setModalQuiz] = useState(null)
  useEffect(()=>{ getHistory().then(setHistory) }, [])
  const openDetails = async id => { setModalQuiz(await getQuiz(id)); setShowModal(true) }
  return (
    <div>
      <table className="w-full mb-6"><thead>
        <tr><th>ID</th><th>Title</th><th>Date</th><th>Action</th></tr>
      </thead><tbody>
        {history.map(q => <tr key={q.id}>
          <td>{q.id}</td><td>{q.title}</td><td>{q.date_generated.split("T")[0]}</td>
          <td><button className="btn" onClick={()=>openDetails(q.id)}>Details</button></td>
        </tr>)}
      </tbody></table>
      {showModal && <Modal onClose={()=>setShowModal(false)}><QuizDisplay quiz={modalQuiz}/></Modal>}
    </div>
  )
}
