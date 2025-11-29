# Real-Time Pair Programming Prototype

A full-stack real-time pair-programming web application where two users can collaborate on the same code editor and receive AI-style (mocked) autocomplete suggestions.

## Tech Stack

### Backend
- Python
- FastAPI
- WebSockets
- SQLAlchemy (Async)
- PostgreSQL (Neon DB)

### Frontend
- React
- TypeScript
- Redux Toolkit
- Vite
# Architecture and Design Choices

## Overall Architecture

The application follows a **client-server architecture** combining REST APIs and WebSockets for efficient communication and real-time collaboration.

### Communication Strategy

- **REST APIs**
  - Handle room creation and management.
  - Serve AI autocomplete responses.

- **WebSockets**
  - Provide real-time bidirectional communication.
  - Broadcast code updates to all users in a room instantly.

- **Database**
  - PostgreSQL is used for persistent storage.
  - Stores room state for crash recovery and reliability.

- **Separation of Concerns**
  - Frontend communicates via REST for tools and WebSocket for live updates.
  - Keeps responsibilities clean and modular.

---

## Backend Design

### FastAPI Framework

FastAPI is used as the backend framework because:

- Async-first performance model.
- Built-in WebSocket support.
- Rapid development with production-grade capability.

---

### WebSockets for Real-Time Collaboration

- Enables low-latency synchronization.
- All users receive updates instantly.
- The server broadcasts updates to every connected client.

---

### Connection Manager

A centralized **Connection Manager** manages WebSocket rooms:

- Maintains connected clients per room.
- Uses broadcast distribution of changes.
- Implements **Last-Write-Wins (LWW)** synchronization:
  - Simple and consistent.
  - Eliminates complex merge logic.
  - Suitable for early-stage prototypes.

---

### Async SQLAlchemy + PostgreSQL

- Non-blocking database operations.
- Stores room state and metadata.
- Enables persistence and crash recovery.

---

## Frontend Design

### React + Hooks

- Component-driven UI development.
- Clear separation between UI and business logic.
- Improves readability and maintainability.

---

### Redux Toolkit

- Centralized state management.
- Predictable data flow.
- Debugging using Redux DevTools.
- Future-ready for scaling.

---

### Debounced Autocomplete

- Prevents excessive backend calls.
- Improves performance and response time.
- Enhances user experience.

---

### Transport Separation

- **WebSockets** → Real-time sync.
- **REST APIs** → Room control and autocomplete.
- Improves maintainability and debugging.

---

## Database Design

### Rooms Table

Single table design:

- `room_id`
- `language`
- `code`

---

### Persistence Flow

- WebSocket updates editor in real time.
- Database periodically stores latest state.
- On reconnect, state is restored from DB.

---


### Improvements With More Time

- Authentication system
- Redis for real-time concurrency scaling
- Real AI model integration
- Version history
- Undo support

### Limitations

- Basic sync model (no merge resolution)
- No authentication
- Single node WebSocket server
- Mock AI only
