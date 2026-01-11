import { useState } from "react";
import GenerateQuiz from "./components/GenerateQuiz";
import History from "./components/History";

export default function App() {
  const [tab, setTab] = useState("generate");

  return (
    <div style={{ padding: 20 }}>
      <h2>AI Wiki Quiz Generator</h2>

      <button onClick={() => setTab("generate")}>Generate Quiz</button>
      <button onClick={() => setTab("history")}>History</button>

      <hr />

      {tab === "generate" ? <GenerateQuiz /> : <History />}
    </div>
  );
}
