import { useEffect, useState } from "react";
import { getPortfolio, sendMessage } from "./api";
import RequestFlow from "./RequestFlow.jsx";

function Rich({ text }) {
  return String(text || "").split(/(\[[^\]]+\])/).map((p, i) =>
    /^\[.*\]$/.test(p) ? <span className="ph" key={i}>{p}</span> : p
  );
}

function Tags({ items }) {
  if (!items || !items.length) return null;
  return <ul className="tg">{items.map((t) => <li key={t}>{t}</li>)}</ul>;
}

function Head({ eye, title, sub }) {
  return (
    <>
      <p className="eye mono">{eye}</p>
      <h2>{title}</h2>
      {sub && <p className="sub">{sub}</p>}
    </>
  );
}

const SNIPPETS = [
  ['@api.depends("order_line")', "30px", "4%"],
  ['self.env["hr.leave"]', "110px", "12%"],
  ['_inherit = "account.move"', "190px", "2%"],
  ['t-esc="record.name"', "270px", "9%"],
];

function Contact({ profile }) {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [status, setStatus] = useState("idle"); // idle | sending | sent | error
  const [error, setError] = useState("");
  const update = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  async function submit(e) {
    e.preventDefault();
    setStatus("sending");
    try {
      await sendMessage(form);
      setForm({ name: "", email: "", message: "" });
      setStatus("sent");
    } catch (err) {
      setError(err.message);
      setStatus("error");
    }
  }

  return (
    <section id="contact">
      <Head eye="Contact" title="Let’s talk."
        sub="Open to Mid-Level Odoo Developer opportunities. Let's connect!." />
      <div className="g">
        <div className="c"><h3>Email</h3><p><a href={`mailto:${profile.email}`}>{profile.email}</a></p></div>
        {profile.phone && <div className="c"><h3>Phone</h3><p><a href={`tel:${profile.phone.replace(/\s/g, "")}`}>{profile.phone}</a></p></div>}
        <div className="c"><h3>Code</h3><p>
          {profile.gitlab && <> · <a href={profile.gitlab}>GitLab</a></>}
          {profile.linkedin && <> · <a href={profile.linkedin}>LinkedIn</a></>}
        </p></div>
      </div>
      <form onSubmit={submit} className="form">
        <label>Name<input name="name" value={form.name} onChange={update} required /></label>
        <label>Email<input name="email" type="email" value={form.email} onChange={update} required /></label>
        <label>Message<textarea name="message" rows="4" value={form.message} onChange={update} required /></label>
        <button className="btn p" disabled={status === "sending"}>{status === "sending" ? "Sending..." : "Send message"}</button>
        {status === "sent" && <p role="status">Message sent. Thank you.</p>}
        {status === "error" && <p role="alert" className="err">{error}</p>}
      </form>
    </section>
  );
}

export default function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    getPortfolio().then(setData).catch((e) => setError(e.message));
  }, []);

  if (error) return <p className="w err">{error}. Is the Django server running?</p>;
  if (!data) return <p className="w">Loading...</p>;
  if (!data.profile) return <p className="w">No profile yet. Run <code>python manage.py seed</code> in the api folder.</p>;

  const { profile: p, about, experience, modules, framework, tools } = data;

  return (
    <>
      <nav className="n" aria-label="Main">
        <div className="w">
          <a className="logo" href="#top">{p.name.split(" ")[0]}.</a>
          <div className="links">
            {["about", "experience", "modules", "framework", "tools", "contact"].map((id) => (
              <a key={id} href={`#${id}`}>{id[0].toUpperCase() + id.slice(1)}</a>
            ))}
          </div>
        </div>
      </nav>

      <main id="top"><div className="w">
        <div className="hero">
          {SNIPPETS.map(([t, top, right]) => (
            <span key={t} className="fl mono" style={{ top, right }}>{t}</span>
          ))}
          <div className="term mono">{p.name.split(" ")[0].toLowerCase()}@erp:<b>~$</b> whoami</div>
          {p.availability && <p className="badge"><i></i> {p.availability}</p>}
          <h1>{p.name}</h1>
          <div className="role">{p.role}</div>
          <p className="lead">{p.intro}</p>
          <a className="btn" href="#contact">Contact</a>
          <ul className="chips">{p.chips.map((c) => <li key={c}>{c}</li>)}</ul>
        </div>

        <section id="about">
          <Head eye="About" title="Backend work with the business in mind."
            sub="Most ERP problems are process problems first. I try to understand the process, then keep the code simple." />
          <div className="g">
            {about.map((a) => <div className="c" key={a.id}><h3>{a.title}</h3><p>{a.text}</p></div>)}
          </div>
        </section>

        <section id="experience">
          <Head eye="Experience" title="Career timeline." sub="About 2.5 years in total." />
          <div className="tl">
            {experience.map((x) => (
              <article key={x.id}>
                <div className="d mono"><Rich text={x.period} /></div>
                <h3>{x.role}</h3>
                <div className="co"><Rich text={x.company} /></div>
                <p>{x.description}</p>
                <Tags items={x.tags} />
              </article>
            ))}
          </div>
        </section>


        <section id="modules">
          <div className="mod-box">
            <p className="mod-eye">Modules I know business-side, not just code-side</p>
            <div className="chips">
              {modules.map((m) => (
                <span className="chip" key={m.id}>{m.name}</span>
              ))}
            </div>
          </div>
        </section>

        <section id="framework">
          <Head eye="Framework" title="Deep in the framework."
            sub="What I do inside Odoo, beyond clicking through the settings." />
          <div className="g">
            {framework.map((f) => <div className="c" key={f.id}><h3>{f.title}</h3><p>{f.description}</p></div>)}
          </div>
          <div className="gap"><RequestFlow /></div>

          <h3 className="sh">The way I write a model</h3>
          <div className="rf"><pre className="code">{`# Small sample pattern (not company code)
from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    unreconciled_line_count = fields.Integer(
        compute="_compute_unreconciled_line_count", store=True
    )

    @api.depends("line_ids.reconciled", "line_ids.account_id.reconcile")
    def _compute_unreconciled_line_count(self):
        for move in self:
            move.unreconciled_line_count = len(
                move.line_ids.filtered(
                    lambda l: l.account_id.reconcile and not l.reconciled
                )
            )`}</pre></div>

          <h3 className="sh">A pattern from my API work</h3>
          <div className="rf"><pre className="code">{`# Simplified example (not client code): Odoo 19 JSON-2 API,
# only post invoices that are still in draft
import requests

HEADERS = {
    "Authorization": f"bearer {API_KEY}",
    "X-Odoo-Database": DB,
}

def call(model, method, **payload):
    r = requests.post(f"{URL}/json/2/{model}/{method}",
                      headers=HEADERS, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()

moves = call("account.move", "search_read",
             domain=[("id", "in", move_ids), ("state", "=", "draft")],
             fields=["name", "partner_id", "amount_total"])

if moves:
    call("account.move", "action_post", ids=[m["id"] for m in moves])`}</pre></div>
        </section>
        <section id="tools">
          <Head eye="Tools" title="Tools I work with daily." sub="From my real work and projects." />
          <div className="g">
            {tools.map((t) => (
              <div className="c" key={t.id}><h3>{t.title}</h3><ul>{t.items.map((i) => <li key={i}>{i}</li>)}</ul></div>
            ))}
          </div>
        </section>

        <section id="education">
          <Head eye="Education" title="Credentials." />
          <div className="g">
            <div className="c"><h3>{p.degree}</h3><p>{p.institution}</p></div>
            <div className="c"><h3>Name on documents</h3><p>{p.name}.{p.also_known_as && ` Known at work as ${p.also_known_as}.`}</p></div>
          </div>
        </section>

        <Contact profile={p} />
      </div></main>

      <footer><div className="w">© {new Date().getFullYear()} {p.name} · {p.role}</div></footer>
    </>
  );
}
