import { useState, useEffect, useRef, useCallback } from "react";

const STAGES = [
  { key: "synthesizer", label: "Synthesizer", icon: "⚗️", color: "#6366f1" },
  { key: "agent_delta", label: "Ag-Δ Rules", icon: "△", color: "#f59e0b" },
  { key: "agent_rel", label: "Ag-⇄ Kernel", icon: "⇄", color: "#10b981" },
  { key: "agent_proc", label: "Ag-⟳ Archetypes", icon: "⟳", color: "#8b5cf6" },
  { key: "tribunal", label: "Tribunal", icon: "⚖️", color: "#64748b" },
  { key: "arbiter", label: "Arbiter", icon: "👁", color: "#ef4444" },
];

const COORD_LABELS = { D: "Dimension", A: "Attribute", X: "Complexity", P: "Polarity" };
const A_NAMES = { "1": "Δ distinction", "2": "⇄ relation", "3": "⟳ process" };
const D_NAMES = { "1": "linear", "2": "planar", "3": "volumetric", "4": "temporal" };
const X_NAMES = { "1": "foundational", "2": "recursive", "3": "synthetic" };

export default function EARMonitor() {
  const [mode, setMode] = useState("idle"); // idle | live | review
  const [wsUrl, setWsUrl] = useState("ws://localhost:8765");
  const [connected, setConnected] = useState(false);
  const [events, setEvents] = useState([]);
  const [stages, setStages] = useState({});
  const [currentConcept, setCurrentConcept] = useState(null);
  const [reviewData, setReviewData] = useState(null);
  const [jsonInput, setJsonInput] = useState("");
  const wsRef = useRef(null);
  const logRef = useRef(null);

  // WebSocket connection
  const connectWs = useCallback(() => {
    try {
      const ws = new WebSocket(wsUrl);
      wsRef.current = ws;

      ws.onopen = () => {
        setConnected(true);
        setMode("live");
        addEvent("system", "Connected to engine");
      };

      ws.onmessage = (e) => {
        const data = JSON.parse(e.data);
        handleEvent(data);
      };

      ws.onclose = () => {
        setConnected(false);
        addEvent("system", "Disconnected");
      };

      ws.onerror = () => {
        setConnected(false);
        addEvent("system", "Connection failed — is the engine running with --monitor?");
      };
    } catch (err) {
      addEvent("system", `Error: ${err.message}`);
    }
  }, [wsUrl]);

  const disconnect = () => {
    if (wsRef.current) wsRef.current.close();
    setConnected(false);
    setMode("idle");
  };

  const addEvent = (type, message, data = null) => {
    setEvents((prev) => [
      ...prev.slice(-100),
      { type, message, data, time: new Date().toLocaleTimeString() },
    ]);
  };

  const handleEvent = (data) => {
    addEvent(data.type, data.stage || data.concept || "event", data);

    if (data.type === "pipeline_start") {
      setCurrentConcept(data.concept);
      setStages({});
    }

    if (data.type === "stage_start") {
      setStages((prev) => ({ ...prev, [data.stage]: { status: "running", start: Date.now() } }));
    }

    if (data.type === "stage_complete") {
      setStages((prev) => ({
        ...prev,
        [data.stage]: {
          ...prev[data.stage],
          status: "complete",
          result: data.result,
          elapsed: Date.now() - (prev[data.stage]?.start || Date.now()),
        },
      }));
    }

    if (data.type === "pipeline_complete") {
      setStages((prev) => ({ ...prev, _final: data.result }));
    }
  };

  // Load JSON for review
  const loadReview = () => {
    try {
      const data = JSON.parse(jsonInput);
      setReviewData(data);
      setMode("review");
      setCurrentConcept(data.concept);
    } catch (err) {
      addEvent("system", `Invalid JSON: ${err.message}`);
    }
  };

  // Auto-scroll log
  useEffect(() => {
    if (logRef.current) logRef.current.scrollTop = logRef.current.scrollHeight;
  }, [events]);

  const getAgentData = (agentKey) => {
    if (mode === "review" && reviewData) return reviewData.agents?.[agentKey];
    return stages[`agent_${agentKey === "delta" ? "delta" : agentKey === "rel" ? "rel" : "proc"}`]?.result;
  };

  const getTribunalData = () => {
    if (mode === "review" && reviewData) return reviewData.tribunal;
    return stages._final ? { ...stages._final, votes: [] } : null;
  };

  const getArbiterData = () => {
    if (mode === "review" && reviewData) return reviewData.arbiter;
    return stages.arbiter?.result;
  };

  return (
    <div style={{ fontFamily: "'Inter', system-ui, sans-serif", background: "#0f172a", color: "#e2e8f0", minHeight: "100vh", padding: 20 }}>
      {/* Header */}
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 20, borderBottom: "1px solid #1e293b", paddingBottom: 16 }}>
        <div>
          <h1 style={{ margin: 0, fontSize: 22, fontWeight: 700, letterSpacing: 1 }}>
            <span style={{ color: "#f59e0b" }}>△</span>
            <span style={{ color: "#10b981" }}>⇄</span>
            <span style={{ color: "#8b5cf6" }}>⟳</span>
            {" "}EAR Triangulation Monitor
          </h1>
          <div style={{ color: "#64748b", fontSize: 12, marginTop: 4 }}>
            {mode === "live" && connected ? "🟢 LIVE" : mode === "review" ? "📋 REVIEW" : "⚪ IDLE"}
            {currentConcept && <span style={{ marginLeft: 12, color: "#94a3b8" }}>→ {currentConcept}</span>}
          </div>
        </div>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          {!connected && (
            <>
              <input
                value={wsUrl}
                onChange={(e) => setWsUrl(e.target.value)}
                style={{ background: "#1e293b", border: "1px solid #334155", borderRadius: 6, padding: "6px 10px", color: "#e2e8f0", fontSize: 12, width: 200 }}
                placeholder="ws://localhost:8765"
              />
              <button onClick={connectWs} style={btnStyle("#10b981")}>Connect Live</button>
            </>
          )}
          {connected && <button onClick={disconnect} style={btnStyle("#ef4444")}>Disconnect</button>}
        </div>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
        {/* Left: Pipeline + Agents */}
        <div>
          {/* Pipeline stages */}
          <div style={panelStyle}>
            <h3 style={panelTitle}>Pipeline</h3>
            <div style={{ display: "flex", gap: 4, alignItems: "center" }}>
              {STAGES.map((s, i) => {
                const st = stages[s.key];
                const isActive = st?.status === "running";
                const isDone = st?.status === "complete";
                const isArbiter = s.key === "arbiter";
                const skip = isArbiter && !getArbiterData() && mode === "review";
                return (
                  <div key={s.key} style={{ display: "flex", alignItems: "center" }}>
                    <div
                      style={{
                        padding: "8px 12px",
                        borderRadius: 8,
                        fontSize: 12,
                        fontWeight: 600,
                        background: isDone ? s.color + "33" : isActive ? s.color + "55" : skip ? "#1e293b44" : "#1e293b",
                        border: `1px solid ${isDone ? s.color : isActive ? s.color : "#334155"}`,
                        color: skip ? "#475569" : isDone ? s.color : "#94a3b8",
                        animation: isActive ? "pulse 1.5s infinite" : "none",
                        opacity: skip ? 0.4 : 1,
                        textAlign: "center",
                        minWidth: 60,
                      }}
                    >
                      <div style={{ fontSize: 16 }}>{s.icon}</div>
                      <div style={{ marginTop: 2 }}>{s.label}</div>
                      {isDone && st?.elapsed && <div style={{ fontSize: 10, opacity: 0.7 }}>{(st.elapsed / 1000).toFixed(1)}s</div>}
                    </div>
                    {i < STAGES.length - 1 && <span style={{ color: "#334155", margin: "0 2px" }}>→</span>}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Three agents side by side */}
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 10, marginTop: 12 }}>
            <AgentCard agent="delta" label="Ag-Δ Rules" color="#f59e0b" data={getAgentData("delta")} />
            <AgentCard agent="rel" label="Ag-⇄ Kernel" color="#10b981" data={getAgentData("rel")} />
            <AgentCard agent="proc" label="Ag-⟳ Archetypes" color="#8b5cf6" data={getAgentData("proc")} />
          </div>

          {/* Tribunal */}
          <TribunalPanel data={getTribunalData()} />

          {/* Arbiter */}
          {getArbiterData() && <ArbiterPanel data={getArbiterData()} />}
        </div>

        {/* Right: Log + JSON loader */}
        <div>
          {/* JSON Review Loader */}
          <div style={panelStyle}>
            <h3 style={panelTitle}>Load Result JSON</h3>
            <textarea
              value={jsonInput}
              onChange={(e) => setJsonInput(e.target.value)}
              placeholder='Paste a result JSON here to review...'
              style={{ width: "100%", height: 100, background: "#0f172a", border: "1px solid #334155", borderRadius: 6, color: "#94a3b8", padding: 8, fontSize: 11, fontFamily: "monospace", resize: "vertical", boxSizing: "border-box" }}
            />
            <button onClick={loadReview} style={{ ...btnStyle("#6366f1"), marginTop: 6, width: "100%" }}>Load & Review</button>
          </div>

          {/* Event Log */}
          <div style={{ ...panelStyle, marginTop: 12 }}>
            <h3 style={panelTitle}>Event Log</h3>
            <div ref={logRef} style={{ maxHeight: 400, overflow: "auto", fontFamily: "monospace", fontSize: 11 }}>
              {events.length === 0 && <div style={{ color: "#475569", padding: 12 }}>Waiting for events... Connect to engine or load a JSON.</div>}
              {events.map((ev, i) => (
                <div key={i} style={{ padding: "3px 0", borderBottom: "1px solid #1e293b11", display: "flex", gap: 8 }}>
                  <span style={{ color: "#475569", minWidth: 70 }}>{ev.time}</span>
                  <span style={{ color: ev.type === "system" ? "#ef4444" : ev.type.includes("complete") ? "#10b981" : "#f59e0b" }}>
                    {ev.type}
                  </span>
                  <span style={{ color: "#94a3b8" }}>{ev.message}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Final Result */}
          {(stages._final || (reviewData?.final)) && (
            <FinalPanel data={stages._final || reviewData?.final} concept={currentConcept} />
          )}
        </div>
      </div>

      <style>{`
        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.6; }
        }
      `}</style>
    </div>
  );
}

// ─── Sub-components ───

function AgentCard({ agent, label, color, data }) {
  if (!data) return (
    <div style={{ ...panelStyle, borderColor: "#1e293b", opacity: 0.4 }}>
      <h4 style={{ margin: 0, fontSize: 13, color }}>{label}</h4>
      <div style={{ color: "#475569", fontSize: 11, marginTop: 8 }}>Waiting...</div>
    </div>
  );

  const coords = data.coordinates || {};
  const sigma = data.sigma || "?";
  const isConstraint = data.type === "constraint";

  return (
    <div style={{ ...panelStyle, borderColor: color + "66" }}>
      <h4 style={{ margin: 0, fontSize: 13, color }}>{label}</h4>
      <div style={{ textAlign: "center", margin: "10px 0", fontSize: 20, fontWeight: 700, color, letterSpacing: 1 }}>
        {isConstraint ? `⚡ ${data.constraint_ref || "CONSTRAINT"}` : sigma}
      </div>
      {!isConstraint && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 4, fontSize: 11 }}>
          <CoordBadge label="D" value={coords.D} decode={D_NAMES[String(coords.D)]} />
          <CoordBadge label="A" value={coords.A} decode={A_NAMES[String(coords.A)]} />
          <CoordBadge label="X" value={coords.X} decode={X_NAMES[String(coords.X)]} />
          <CoordBadge label="P" value={coords.P} decode={coords.P === "+" ? "expand" : "contract"} />
        </div>
      )}
      {data.confidence_notes && (
        <div style={{ marginTop: 8, fontSize: 10, color: "#94a3b8", borderTop: "1px solid #1e293b", paddingTop: 6 }}>
          {data.confidence_notes}
        </div>
      )}
    </div>
  );
}

function CoordBadge({ label, value, decode }) {
  return (
    <div style={{ background: "#1e293b", borderRadius: 4, padding: "3px 6px", textAlign: "center" }}>
      <span style={{ color: "#64748b" }}>{label}=</span>
      <span style={{ color: "#e2e8f0", fontWeight: 600 }}>{value}</span>
      {decode && <div style={{ fontSize: 9, color: "#64748b" }}>{decode}</div>}
    </div>
  );
}

function TribunalPanel({ data }) {
  if (!data) return null;
  const votes = data.votes || [];
  const verdict = data.verdict || data.status;
  const verdictColor = verdict === "VALID" ? "#10b981" : verdict === "REVIEW" ? "#f59e0b" : "#ef4444";

  return (
    <div style={{ ...panelStyle, marginTop: 12, borderColor: "#64748b66" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h3 style={panelTitle}>⚖️ Tribunal</h3>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <span style={{ fontSize: 13, fontWeight: 700, color: verdictColor }}>{verdict}</span>
          <span style={{ fontSize: 20, fontWeight: 700, color: "#e2e8f0" }}>{data.sigma}</span>
          <span style={{ fontSize: 12, color: "#94a3b8" }}>conf: {(data.confidence || 0).toFixed(2)}</span>
        </div>
      </div>
      {votes.length > 0 && (
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr 1fr", gap: 6, marginTop: 10 }}>
          {votes.map((v) => (
            <div key={v.coord} style={{
              background: v.unanimous ? "#10b98122" : "#f59e0b22",
              border: `1px solid ${v.unanimous ? "#10b98155" : "#f59e0b55"}`,
              borderRadius: 6, padding: 8, textAlign: "center"
            }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: v.unanimous ? "#10b981" : "#f59e0b" }}>
                {v.coord}={v.majority}
              </div>
              <div style={{ fontSize: 10, color: "#94a3b8", marginTop: 2 }}>
                {v.unanimous ? "✓ unanimous" : `⚠ ${v.dissenter} → ${v.dissenter_value}`}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function ArbiterPanel({ data }) {
  const analyses = data?.analysis || [];
  const final = data?.final_recommendation;

  return (
    <div style={{ ...panelStyle, marginTop: 12, borderColor: "#ef444466" }}>
      <h3 style={panelTitle}>👁 Arbiter — Blind Spot Analysis</h3>
      {analyses.map((a, i) => (
        <div key={i} style={{ background: "#1e293b", borderRadius: 6, padding: 8, marginTop: 6, fontSize: 11 }}>
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <span style={{ fontWeight: 700, color: "#e2e8f0" }}>{a.coordinate}: {a.agent_dissents} dissents</span>
            <span style={{
              color: a.dissent_in_blind_spot ? "#10b981" : "#ef4444",
              fontWeight: 600
            }}>
              {a.dissent_in_blind_spot ? "BLIND SPOT → majority OK" : "⚠ GENUINE → review"}
            </span>
          </div>
          <div style={{ color: "#94a3b8", marginTop: 4 }}>{a.explanation}</div>
          <div style={{ color: a.recommendation === "ACCEPT_MAJORITY" ? "#10b981" : "#f59e0b", marginTop: 2, fontWeight: 600, fontSize: 10 }}>
            → {a.recommendation}
          </div>
        </div>
      ))}
      {final && (
        <div style={{ marginTop: 8, padding: 8, background: "#0f172a", borderRadius: 6, textAlign: "center" }}>
          <span style={{ fontSize: 16, fontWeight: 700, color: "#e2e8f0" }}>{final.sigma}</span>
          <span style={{ marginLeft: 12, color: final.status === "VALID" ? "#10b981" : "#f59e0b", fontWeight: 600 }}>
            {final.status}
          </span>
          <span style={{ marginLeft: 8, color: "#64748b", fontSize: 11 }}>conf: {final.confidence}</span>
          <div style={{ color: "#94a3b8", fontSize: 11, marginTop: 4 }}>{final.reason}</div>
        </div>
      )}
    </div>
  );
}

function FinalPanel({ data, concept }) {
  if (!data) return null;
  const statusColor = data.status === "VALID" ? "#10b981" : data.status === "REVIEW" ? "#f59e0b" : "#ef4444";
  return (
    <div style={{ ...panelStyle, marginTop: 12, borderColor: statusColor + "66", background: "#0f172a" }}>
      <div style={{ textAlign: "center" }}>
        <div style={{ fontSize: 12, color: "#64748b", marginBottom: 4 }}>{concept}</div>
        <div style={{ fontSize: 28, fontWeight: 800, color: "#e2e8f0", letterSpacing: 2 }}>{data.sigma}</div>
        <div style={{ marginTop: 6 }}>
          <span style={{ background: statusColor + "33", color: statusColor, padding: "4px 12px", borderRadius: 20, fontSize: 13, fontWeight: 700 }}>
            {data.status}
          </span>
          <span style={{ marginLeft: 12, color: "#94a3b8", fontSize: 13 }}>
            confidence: {(data.confidence || 0).toFixed(2)}
          </span>
        </div>
      </div>
    </div>
  );
}

// ─── Styles ───

const panelStyle = {
  background: "#1e293b",
  borderRadius: 10,
  padding: 14,
  border: "1px solid #334155",
};

const panelTitle = {
  margin: "0 0 10px 0",
  fontSize: 13,
  fontWeight: 600,
  color: "#94a3b8",
  letterSpacing: 0.5,
};

function btnStyle(color) {
  return {
    background: color + "22",
    color,
    border: `1px solid ${color}55`,
    borderRadius: 6,
    padding: "6px 14px",
    fontSize: 12,
    fontWeight: 600,
    cursor: "pointer",
  };
}
