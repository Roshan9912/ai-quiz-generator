import { useEffect, useState } from "react";
import { getHistory } from "../api";
import QuizModal from "./QuizModal";

export default function History() {
  const [items, setItems] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    getHistory().then(setItems);
  }, []);

  return (
    <div>
      <h3>Past Quizzes</h3>

      <table border="1">
        <tbody>
          {items.map((q) => (
            <tr key={q.id}>
              <td>{q.title}</td>
              <td>
                <button onClick={() => setSelected(q)}>Details</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selected && (
        <QuizModal data={selected} onClose={() => setSelected(null)} />
      )}
    </div>
  );
}
