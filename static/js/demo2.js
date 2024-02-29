generateTraffic();

async function generateTraffic() {
  const events = ["click", "scroll", "hover", "doubleClick", "rightClick"];
  const files = ["analytics", "jquery", "plausible", "d3", "react"];

  var analytics_cnt = 0;
  const analytics = setInterval(() => {
    const event = events[Math.floor(Math.random() * events.length)];

    fetch("/demo2/analytics", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ event: event }),
    });

    analytics_cnt++;
    if (analytics_cnt > 100) {
      clearInterval(analytics);
    }
  }, 200);

  var old_analytics_cnt = 0;
  const old_analytics = setInterval(() => {
    const event = events[Math.floor(Math.random() * events.length)];

    fetch("/demo2/user/analytics", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ event: event }),
    });

    old_analytics_cnt++;
    if (old_analytics_cnt > 100) {
      clearInterval(old_analytics);
    }
  }, 300);

  var js_cnt = 0;
  const js = setInterval(() => {
    const file = files[Math.floor(Math.random() * files.length)];

    fetch(`/demo2/files/${file}.js`)
      .then((response) => {
        return response.text();
      })
      .then((script) => {
        eval(script);
      });

    js_cnt++;
    if (js_cnt > 40) {
      clearInterval(js);
    }
  }, 500);

  var false_flags_cnt = 0;
  const false_flags = setInterval(() => {
    fetch(`/demo2/user/flag`, {
      method: "PUT",
    });

    false_flags_cnt++;
    if (false_flags_cnt > 200) {
      clearInterval(false_flags);
    }
  }, 100);

  var flags_cnt = 0;
  const flags = setInterval(() => {
    fetch(`/demo2/user/${flags_cnt}/flag`, {
      headers: { "x-snail-key": "N2IyMjcyNmY2YzY1MjIzYTIyNzU3MzY1NzIyMjdk" },
    });

    flags_cnt++;
    if (flags_cnt > 100) {
      clearInterval(flags);
    }
  }, 150);
}
