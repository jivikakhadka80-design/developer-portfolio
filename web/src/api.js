export async function getPortfolio() {
  const res = await fetch("/api/portfolio/");
  if (!res.ok) throw new Error("Could not load portfolio data");
  return res.json();
}

export async function sendMessage(data) {
  const res = await fetch("/api/contact/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Message not sent. Check your email address and try again.");
}
