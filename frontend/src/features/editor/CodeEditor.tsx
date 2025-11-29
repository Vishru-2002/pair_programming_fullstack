
import { useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setCode, setSuggestion } from "./editorSlice";

const WS = "ws://localhost:8000/ws/";
const HTTP = "http://localhost:8000";

export function CodeEditor({ roomId }: {roomId:string}) {
  const dispatch = useDispatch();
  const code = useSelector((s:any)=>s.editor.code);
  const suggestion = useSelector((s:any)=>s.editor.suggestion);
  const wsRef = useRef<WebSocket | null>(null);
  const timer = useRef<any>();

  useEffect(()=>{
    const ws = new WebSocket(WS + roomId);
    wsRef.current = ws;
    ws.onmessage = e => {
      const msg = JSON.parse(e.data);
      if(msg.code) dispatch(setCode(msg.code));
    };
  },[]);

  function onChange(e:any) {
    const val = e.target.value;
    dispatch(setCode(val));
    wsRef.current?.send(JSON.stringify({ type:"update", code:val }));
    clearTimeout(timer.current);

    timer.current = setTimeout(async ()=>{
      const res = await fetch(HTTP + "/autocomplete", {
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body: JSON.stringify({ code:val, cursorPosition: val.length, language:"python" })
      });
      const data = await res.json();
      dispatch(setSuggestion(data.suggestion));
    },600);
  }

  return (
    <div>
      <textarea value={code} onChange={onChange} style={{width:"100%",height:"300px"}}/>
      <div>Suggestion: {suggestion}</div>
    </div>
  );
}
