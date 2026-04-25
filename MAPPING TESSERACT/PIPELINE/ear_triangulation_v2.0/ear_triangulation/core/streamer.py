"""
EAR Triangulation Engine — Event Streamer
Lightweight WebSocket server that streams pipeline events to the monitor dashboard.
Zero interference with the mapping logic.
"""

import json
import asyncio
import threading
from datetime import datetime, timezone
from typing import Optional

# Will be set when server starts
_ws_connections = set()
_event_queue = asyncio.Queue() if False else None  # lazy init
_loop = None


class EventStreamer:
    """
    Drop-in event streamer. Attach to TriangulationEngine to broadcast events.
    If no dashboard is connected, events are silently dropped (zero overhead).
    """
    
    def __init__(self, port: int = 8765):
        self.port = port
        self.enabled = False
        self._server_thread = None
        self._loop = None
        self._connections = set()
        self._queue = None
    
    def start(self):
        """Start WebSocket server in background thread."""
        self._server_thread = threading.Thread(target=self._run_server, daemon=True)
        self._server_thread.start()
        self.enabled = True
        print(f"[MONITOR] WebSocket server started on ws://localhost:{self.port}")
        print(f"[MONITOR] Open the dashboard to watch the process live.")
    
    def _run_server(self):
        import asyncio
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._queue = asyncio.Queue()
        self._loop.run_until_complete(self._serve())
    
    async def _serve(self):
        try:
            import websockets
        except ImportError:
            print("[MONITOR] pip install websockets to enable live monitoring")
            return
        
        async def handler(ws, path=None):
            self._connections.add(ws)
            try:
                # Send welcome
                await ws.send(json.dumps({
                    "type": "connected",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "message": "EAR Triangulation Monitor connected"
                }))
                # Keep alive until disconnect
                async for msg in ws:
                    pass  # We don't expect messages from dashboard
            finally:
                self._connections.discard(ws)
        
        # Start broadcast task
        asyncio.ensure_future(self._broadcaster())
        
        async with websockets.serve(handler, "0.0.0.0", self.port):
            await asyncio.Future()  # Run forever
    
    async def _broadcaster(self):
        """Send queued events to all connected dashboards."""
        while True:
            event = await self._queue.get()
            if self._connections:
                payload = json.dumps(event, default=str, ensure_ascii=False)
                dead = set()
                for ws in self._connections:
                    try:
                        await ws.send(payload)
                    except Exception:
                        dead.add(ws)
                self._connections -= dead
    
    def emit(self, event_type: str, data: dict = None):
        """
        Emit an event. Non-blocking. If no server or no connections, silently drops.
        """
        if not self.enabled or not self._loop or not self._queue:
            return
        
        event = {
            "type": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            **(data or {})
        }
        
        # Thread-safe put
        asyncio.run_coroutine_threadsafe(
            self._queue.put(event),
            self._loop
        )


# ─── Integration helper ───

def patch_engine_with_streaming(engine, port: int = 8765):
    """
    Monkey-patch a TriangulationEngine to emit events.
    Zero changes to original code needed.
    """
    streamer = EventStreamer(port=port)
    streamer.start()
    engine._streamer = streamer
    
    # Wrap each pipeline method
    original_synthesize = engine.synthesize
    original_agent_delta = engine.run_agent_delta
    original_agent_rel = engine.run_agent_rel
    original_agent_proc = engine.run_agent_proc
    original_arbiter = engine.run_arbiter
    
    def wrapped_synthesize(concept, domain=""):
        streamer.emit("stage_start", {"stage": "synthesizer", "concept": concept, "domain": domain})
        result = original_synthesize(concept, domain)
        streamer.emit("stage_complete", {"stage": "synthesizer", "result": result})
        return result
    
    def wrapped_agent_delta(synthesis):
        streamer.emit("stage_start", {"stage": "agent_delta", "input": synthesis.get("concept", "")})
        result = original_agent_delta(synthesis)
        streamer.emit("stage_complete", {"stage": "agent_delta", "result": result})
        return result
    
    def wrapped_agent_rel(synthesis):
        streamer.emit("stage_start", {"stage": "agent_rel", "input": synthesis.get("concept", "")})
        result = original_agent_rel(synthesis)
        streamer.emit("stage_complete", {"stage": "agent_rel", "result": result})
        return result
    
    def wrapped_agent_proc(synthesis):
        streamer.emit("stage_start", {"stage": "agent_proc", "input": synthesis.get("concept", "")})
        result = original_agent_proc(synthesis)
        streamer.emit("stage_complete", {"stage": "agent_proc", "result": result})
        return result
    
    def wrapped_arbiter(tribunal_result):
        streamer.emit("stage_start", {"stage": "arbiter", "disagreement": tribunal_result.disagreement_summary})
        result = original_arbiter(tribunal_result)
        streamer.emit("stage_complete", {"stage": "arbiter", "result": result})
        return result
    
    engine.synthesize = wrapped_synthesize
    engine.run_agent_delta = wrapped_agent_delta
    engine.run_agent_rel = wrapped_agent_rel
    engine.run_agent_proc = wrapped_agent_proc
    engine.run_arbiter = wrapped_arbiter
    
    # Also emit tribunal results
    original_map = engine.map_concept
    def wrapped_map(concept, domain=""):
        streamer.emit("pipeline_start", {"concept": concept, "domain": domain})
        result = original_map(concept, domain)
        streamer.emit("pipeline_complete", {"concept": concept, "result": result.get("final", {})})
        return result
    
    engine.map_concept = wrapped_map
    
    return streamer
