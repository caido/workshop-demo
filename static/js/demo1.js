send_flag();

async function send_flag() {
  generate_junk();

  fetch("/demo1/flag", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ flag: "CO-ThisIsANiceSnail" }),
  });

  generate_junk();
}

async function generate_junk() {
  for (let i = 0; i < 10; i++) {
    fetch(`/demo1/junk/${i}`);
  }
}
