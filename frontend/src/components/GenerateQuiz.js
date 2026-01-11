import { useState } from "react";
import { generateQuiz } from "../api";
import QuizCard from "./QuizCard";

export default function GenerateQuiz() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    const json = await generateQuiz(url);
    if (json.detail) {
  alert(json.detail);
  setData(json);
  setLoading(false);
  return;
}
    setData(json);
    setLoading(false);
  };

  return (
    <div>
      <input
        placeholder="Wikipedia URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "60%" }}
      />
      <button onClick={handleGenerate}>Generate</button>

      {loading && <p>Generating quiz...</p>}
      {data && <QuizCard data={data} />}
    </div>
  );
}
