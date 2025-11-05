import React, { useState } from 'react'
import GenerateQuizTab from './tabs/GenerateQuizTab'
import HistoryTab from './tabs/HistoryTab'

export default function App() {
  const [activeTab, setActiveTab] = useState('generate')
  return (
    <div className="bg-gray-100 min-h-screen">
      <div className="flex gap-3 border-b p-4 font-bold">
        <button onClick={() => setActiveTab('generate')}>Generate Quiz</button>
        <button onClick={() => setActiveTab('history')}>History</button>
      </div>
      <div className="p-4">{activeTab === 'generate' ? <GenerateQuizTab /> : <HistoryTab />}</div>
    </div>
  )
}
