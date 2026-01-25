import { useEffect, useState } from "react";
import { getHistory } from "../api";

function History() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    getHistory().then(setItems).catch(console.error);
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Past Quizzes</h2>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>URL</th>
            <th>Title</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.url}</td>
              <td>{item.title}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default History;
