import { useEffect, useState } from "react";
import { getHistory } from "../api";

export default function History() {
  const [data, setData] = useState([]);

  useEffect(() => {
    getHistory().then(setData);
  }, []);

  return (
    <table>
      <tbody>
        {data.map(q => (
          <tr key={q.id}>
            <td>{q.title}</td>
            <td>{q.url}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
