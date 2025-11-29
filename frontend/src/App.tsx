
import { BrowserRouter, Routes, Route, useParams, useNavigate } from "react-router-dom";
import { CodeEditor } from "./features/editor/CodeEditor";

const BACKEND = "http://localhost:8000";

function Home() {
  const nav = useNavigate();
  async function createRoom() {
    const res = await fetch(BACKEND + "/rooms", { method: "POST" });
    const data = await res.json();
    nav("/room/" + data.roomId);
  }
  return <button onClick={createRoom}>Create Room</button>;
}

function Room() {
  const { roomId } = useParams();
  return <CodeEditor roomId={roomId!} />;
}

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/room/:roomId" element={<Room/>}/>
      </Routes>
    </BrowserRouter>
  );
}
