
import { createSlice } from '@reduxjs/toolkit';

const slice = createSlice({
  name: "editor",
  initialState: { code: "", suggestion: "" },
  reducers: {
    setCode: (s,a)=>{ s.code=a.payload; },
    setSuggestion: (s,a)=>{ s.suggestion=a.payload; }
  }
});

export const { setCode, setSuggestion } = slice.actions;
export default slice.reducer;
