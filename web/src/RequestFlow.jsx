import { useRef, useState } from "react";

const STAGES = [
  ["Client", "The employee fills the leave form in the browser."],
  ["Controller", "Odoo routes the call and checks the logged-in user."],
  ["Model", "hr.leave runs its constraints: dates, balance, overlaps."],
  ["ORM", "The recordset is created and caches are updated."],
  ["PostgreSQL", "The row is saved inside one transaction."],
];

export default function RequestFlow() {
  const [active, setActive] = useState(-1);
  const [lines, setLines] = useState(["Press Run request to follow a leave request through Odoo."]);
  const running = useRef(false);

  function show(i) {
    setActive(i);
    setLines([`> ${STAGES[i][0]}: ${STAGES[i][1]}`]);
  }

  function run() {
    if (running.current) return;
    running.current = true;
    setLines([]);
    let i = 0;
    const step = () => {
      if (i >= STAGES.length) {
        setActive(-1);
        setLines((l) => [...l, "> done: leave request saved."]);
        running.current = false;
        return;
      }
      setActive(i);
      setLines((l) => [...l, `> ${STAGES[i][0]}: ${STAGES[i][1]}`]);
      i += 1;
      setTimeout(step, 650);
    };
    step();
  }

  return (
    <div className="rf">
      <div className="mono cm-line">// how an Odoo request flows. Click Run, or click a stage.</div>
      <div className="st">
        {STAGES.map((s, i) => (
          <span key={s[0]} className="st-item">
            <button type="button" className={active === i ? "on" : ""} onClick={() => show(i)}>{s[0]}</button>
            {i < STAGES.length - 1 && <span className="arrow">→</span>}
          </span>
        ))}
      </div>
      <div className="log" aria-live="polite">{lines.map((l, i) => <div key={i}>{l}</div>)}</div>
      <button type="button" className="run" onClick={run}>Run request</button>
    </div>
  );
}
