export default function Modal({ children, onClose }) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
      <div className="bg-white p-8 rounded shadow-md min-w-[320px] max-w-lg">{children}
        <button className="mt-6 px-4 py-2 bg-blue-200 rounded" onClick={onClose}>Close</button>
      </div>
    </div>
  )
}
