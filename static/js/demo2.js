generateTraffic();

async function generateTraffic() {
  const events = ["click", "scroll", "hover", "doubleClick", "rightClick"];
  const files = ["analytics", "jquery", "plausible", "d3", "react"];

  let analytics_cnt = 0;
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
  }, 150);

  let old_analytics_cnt = 0;
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

  let js_cnt = 0;
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
    if (js_cnt > 100) {
      clearInterval(js);
    }
  }, 1000);

  let false_flag_cnt = 0;
  const false_flag = setInterval(() => {
    fetch(`/demo2/user/${false_flag_cnt}/flag`)
      .then((response) => {
        return response.text();
      })
      .then((script) => {
        eval(script);
      });

    false_flag_cnt++;
    if (false_flag_cnt > 200) {
      clearInterval(false_flag);
    }
  }, 100);
}
