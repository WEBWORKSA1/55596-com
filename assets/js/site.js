/* 55596.com — site behaviour: nav, theme, consent, video, forms, decoder and tools UI */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var ROOT = document.documentElement.getAttribute("data-root") || "";
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function params() { var o = {}; location.search.replace(/^\?/, "").split("&").forEach(function (kv) { if (!kv) return; var p = kv.split("="); o[decodeURIComponent(p[0])] = decodeURIComponent((p[1] || "").replace(/\+/g, " ")); }); return o; }

  /* Navigation */
  var mb = $(".menu-btn"), nav = $(".nav");
  if (mb && nav) mb.addEventListener("click", function () { var o = nav.classList.toggle("open"); mb.setAttribute("aria-expanded", o); });

  /* Theme */
  var saved = store("theme"); if (saved) document.documentElement.setAttribute("data-theme", saved);
  $$(".theme-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var nx = cur === "dark" ? "light" : "dark"; document.documentElement.setAttribute("data-theme", nx); store("theme", nx);
    });
  });

  /* Cookie notice */
  if (!store("consent")) {
    var c = document.createElement("div"); c.className = "consent"; c.setAttribute("role", "dialog"); c.setAttribute("aria-label", "Cookie notice");
    c.innerHTML = '<p>We use cookies for essential features and to show ads through Google AdSense, which may personalise ads. Read our <a href="' + ROOT + 'cookies.html">cookie policy</a>.</p><div class="btns"><button class="btn small" data-c="all">Accept all</button><button class="btn small ghost" data-c="essential">Essential only</button></div>';
    document.body.appendChild(c);
    c.addEventListener("click", function (e) { var v = e.target.getAttribute("data-c"); if (!v) return; store("consent", v); if (v === "essential") { (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1; } c.remove(); });
  } else if (store("consent") === "essential") { (window.adsbygoogle = window.adsbygoogle || []).requestNonPersonalizedAds = 1; }

  /* Lite YouTube */
  $$(".video button[data-id]").forEach(function (b) {
    var id = b.getAttribute("data-id");
    b.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    b.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.title = b.getAttribute("aria-label") || "YouTube video"; f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"; f.allowFullscreen = true;
      b.replaceWith(f);
    });
  });

  /* Forms — single endpoint, assembled at runtime so the address never appears in page source */
  var EK = [126, 108, 105, 126, 118, 121, 114, 122, 104, 56, 71, 110, 116, 104, 112, 115, 53, 106, 118, 116];
  function endpoint() { return "https://formsubmit.co/ajax/" + EK.map(function (n) { return String.fromCharCode(n - 7); }).join(""); }
  function validStep(scope) {
    var ok = true;
    $$("input,select,textarea", scope).forEach(function (el) { if (!el.checkValidity()) { if (ok) el.reportValidity(); ok = false; } });
    return ok;
  }
  $$("form[data-form]").forEach(function (form) {
    var status = $(".form-status", form);
    /* multi-step */
    var steps = $$("fieldset[data-step]", form), cur = 0, dots = $$(".steps li", form);
    function show(i) { steps.forEach(function (s, j) { s.hidden = j !== i; }); dots.forEach(function (d, j) { d.classList.toggle("on", j <= i); }); cur = i; var f = steps[i] && $("input,select,textarea", steps[i]); if (f && i) f.focus(); }
    if (steps.length) {
      show(0);
      $$("[data-next]", form).forEach(function (b) { b.addEventListener("click", function () { if (validStep(steps[cur])) show(cur + 1); }); });
      $$("[data-back]", form).forEach(function (b) { b.addEventListener("click", function () { show(cur - 1); }); });
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validStep(form)) return;
      var fd = new FormData(form), data = {};
      fd.forEach(function (v, k) { if (k === "_hp") return; data[k] = data[k] ? data[k] + ", " + v : v; });
      if (fd.get("_hp")) return;
      data._subject = "55596.com — " + (form.getAttribute("data-subject") || "Website form");
      data._template = "table"; data._captcha = "false";
      data["Form"] = form.getAttribute("data-form"); data["Page"] = location.href;
      var btn = $("button[type=submit]", form); if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
      if (status) { status.className = "form-status"; status.textContent = ""; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function () { location.href = ROOT + "thank-you.html?f=" + encodeURIComponent(form.getAttribute("data-form")); })
        .catch(function () {
          if (status) { status.className = "form-status err"; status.textContent = "Your message didn't send. Check your connection and press the button again."; }
          if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; }
        });
    });
  });
  /* Prefill fields from the URL (?need=phone&digits=8888 etc.) */
  var P = params();
  Object.keys(P).forEach(function (k) {
    $$('[name="' + k.replace(/"/g, "") + '"]').forEach(function (el) {
      if (el.type === "radio" || el.type === "checkbox") { if (el.value === P[k]) el.checked = true; }
      else if (!el.value) el.value = P[k];
    });
  });
  if (P.amount) { var a = $('[name="Amount (USD)"]'); if (a) a.value = P.amount; }
  if (P.f) { var t = $("[data-thanks]"); if (t) t.setAttribute("data-kind", P.f); }

  /* Shared renderers */
  var E = window.N55596;
  function keys(str, cls) {
    return '<div class="keys" aria-hidden="true">' + str.split("").map(function (d) {
      var z = window.N_DATA.digits[d].zh.status; return '<span class="key ' + (cls || "") + " " + z + '"><b>' + d + "</b><small>" + (window.N_DATA.keypad[d] || "&nbsp;") + "</small></span>";
    }).join("") + "</div>";
  }
  function ring(v) { return '<div class="score-ring" style="--v:' + v + '"><span>' + v + "</span></div>"; }
  function luckBlock(L, str, kind) {
    var need = kind || "phone";
    return '<div class="score">' + ring(L.score) + '<div><h3 class="mt0">' + esc(L.grade) + " luck score</h3><p class=\"muted mt0\">Chinese homophone tradition plus memorability. For culture and fun, not a guarantee.</p></div></div>" +
      (L.notes.length ? "<ul>" + L.notes.map(function (n) { return "<li>" + esc(n) + "</li>"; }).join("") + "</ul>" : "<p>No strong lucky or unlucky signals — a neutral number.</p>") +
      (L.better.length ? "<p><strong>Luckier variations:</strong> " + L.better.map(function (b) { return '<a class="chip lucky" href="' + ROOT + "decode.html?n=" + b + '">' + b + "</a>"; }).join(" ") + "</p>" : "") +
      '<div class="panel gold mt1"><p class="mt0"><strong>Want a number that scores 85+?</strong> We source lucky and vanity ' + need + ' numbers and numeric domains on request.</p><a class="btn" href="' + ROOT + "lucky-numbers.html?need=" + need + "&digits=" + encodeURIComponent(str) + '">Find me a luckier number</a></div>';
  }

  /* Decoder */
  var dec = $("#decoder");
  if (dec) {
    var inp = $("#decode-input"), out = $("#decode-out");
    var render = function (val) {
      var r = E.decode(val);
      if (!r) { out.innerHTML = '<p class="note">Type a number using digits only — up to 15 digits. Try 555, 520 or your phone number.</p>'; return; }
      if (history.replaceState) history.replaceState(null, "", "?n=" + r.str);
      document.title = r.str + " meaning — Decode any number | 55596";
      var zhRows = r.digits.map(function (d) { return "<tr><td><strong>" + d.d + "</strong></td><td>" + esc(d.zh.char) + " " + esc(d.zh.py) + "</td><td>" + esc(d.zh.sounds) + '</td><td><span class="badge ' + d.zh.status + '">' + d.zh.status + "</span></td></tr>"; }).join("");
      var combos = r.combos.length ? r.combos.map(function (c) { return '<li><span class="badge ' + c.status + '">' + esc(c.code) + "</span> <strong>" + esc(c.region) + ":</strong> " + esc(c.reading) + " — " + esc(c.meaning) + "</li>"; }).join("") : "<li>No famous combinations inside this number.</li>";
      var sl = r.slang.length ? r.slang.map(function (s) { return '<li><strong>' + esc(s.lang) + ":</strong> " + esc(s.meaning) + ' <span class="muted">(' + esc(s.reading) + ") " + esc(s.note) + "</span></li>"; }).join("") : "<li>This exact number isn't a known slang code. Browse the <a href=\"" + ROOT + "slang.html\">slang dictionary</a>.</li>";
      var m = r.math;
      var facts = [["Words", m.words], ["Digits", m.digits], ["Prime?", m.prime === undefined ? "—" : (m.prime ? "Yes" : "No")], ["Prime factors", m.factors || "—"], ["Divisors", m.divisors || "—"], ["Perfect square", m.square ? "Yes, " + m.square + "²" : "No"], ["Palindrome", m.palindrome ? "Yes" : "No"], ["Binary", m.binary], ["Hexadecimal", m.hex], ["Octal", m.octal], ["Roman", m.roman]];
      out.innerHTML =
        '<div class="panel">' + keys(r.str) +
        '<p class="eq">' + r.str.split("").join(" + ") + " = " + r.sum + (r.steps.length > 1 ? " → " + r.steps.slice(1).join(" → ") : "") + "&nbsp; <strong>Root " + r.root + "</strong></p>" +
        '<p class="mt0">' + esc(r.rootMeaning) + ".</p>" +
        (r.page ? '<p><a class="btn small ghost" href="' + ROOT + "number/" + r.page + '/">Read the full guide to ' + r.page + "</a></p>" : "") +
        '<div class="result-tabs" role="tablist">' +
        ["Angel", "Culture", "Slang", "Luck score", "Math"].map(function (t, i) { return '<button role="tab" aria-selected="' + (i === 0) + '" data-t="' + i + '">' + t + "</button>"; }).join("") + "</div>" +
        '<div class="result-pane" data-p="0"><h3>' + esc(r.angel.kind) + "</h3><p>" + esc(r.angel.text) + '</p><p class="muted">Angel-number readings are a spiritual tradition, offered here for reflection and entertainment.</p></div>' +
        '<div class="result-pane" data-p="1" hidden><h3>Digit by digit in Chinese</h3><div class="table-wrap"><table class="table"><thead><tr><th>Digit</th><th>Character</th><th>Sounds like</th><th>Reputation</th></tr></thead><tbody>' + zhRows + '</tbody></table></div><h3 class="mt2">Combinations found</h3><ul>' + combos + "</ul></div>" +
        '<div class="result-pane" data-p="2" hidden><h3>Internet slang matches</h3><ul>' + sl + "</ul></div>" +
        '<div class="result-pane" data-p="3" hidden>' + luckBlock(r.luck, r.str, "phone") + "</div>" +
        '<div class="result-pane" data-p="4" hidden><ul class="facts">' + facts.map(function (f) { return "<li><span>" + f[0] + "</span><b>" + esc(f[1]) + "</b></li>"; }).join("") + "</ul></div></div>";
      $$(".result-tabs button", out).forEach(function (b) {
        b.addEventListener("click", function () {
          $$(".result-tabs button", out).forEach(function (x) { x.setAttribute("aria-selected", x === b); });
          $$(".result-pane", out).forEach(function (p) { p.hidden = p.getAttribute("data-p") !== b.getAttribute("data-t"); });
        });
      });
    };
    $("#decode-form").addEventListener("submit", function (e) { e.preventDefault(); render(inp.value); });
    var start = P.n || inp.value || "55596"; inp.value = start; render(start);
  }

  /* Tools */
  var MEAN = window.N_DATA ? window.N_DATA.digits : {};
  function rootText(n) { return (window.N_DATA.master[String(n)] || (MEAN[String(n)] ? MEAN[String(n)].num : "")); }
  var COMPAT = { "1": [1, 5, 7], "2": [2, 4, 8], "3": [3, 6, 9], "4": [2, 4, 8], "5": [1, 5, 7], "6": [3, 6, 9], "7": [1, 5, 7], "8": [2, 4, 8], "9": [3, 6, 9] };
  $$("form[data-tool]").forEach(function (f) {
    var out = $("[data-out]", f.parentNode) || $("[data-out]");
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var t = f.getAttribute("data-tool"), v = function (n) { var el = f.elements[n]; return el ? el.value : ""; }, html = "";
      if (t === "life-path" || t === "personal-year") {
        var dt = v("dob"); if (!dt) return; var p = dt.split("-");
        if (t === "life-path") {
          var lp = E.lifePath(p[0], +p[1], +p[2]);
          html = keys(String(lp.root)) + '<p class="eq">Month ' + lp.parts[0] + " + Day " + lp.parts[1] + " + Year " + lp.parts[2] + " = " + lp.total + " &nbsp;<strong>Life path " + lp.root + "</strong></p><p>" + esc(rootText(lp.root)) + '.</p><p><a href="' + ROOT + "number/" + (lp.root > 9 ? lp.root : lp.root) + '/">Read about the number ' + lp.root + "</a></p>";
        } else {
          var yr = +v("year") || new Date().getFullYear(), py = E.personalYear(+p[1], +p[2], yr);
          html = keys(String(py)) + "<h3>Your personal year " + py + " (" + yr + ")</h3><p>Theme for the year: " + esc(rootText(py)) + ".</p>";
        }
      } else if (t === "name-number" || t === "business-name") {
        var nm = v("name"); if (!nm.trim()) return; var sys = v("system") || "pythagorean", r = E.nameNumber(nm, sys);
        html = keys(String(r.expression)) + "<h3>" + (t === "business-name" ? "Business name number " : "Expression number ") + r.expression + "</h3><p>" + esc(rootText(r.expression)) + '.</p><ul class="facts"><li><span>Letter total</span><b>' + r.total + "</b></li><li><span>Soul urge (vowels)</span><b>" + r.soul + "</b></li><li><span>Personality (consonants)</span><b>" + r.personality + "</b></li><li><span>System</span><b>" + (sys === "chaldean" ? "Chaldean" : "Pythagorean") + "</b></li></ul>" +
          (t === "business-name" ? '<p class="mt1">Numerology traditions often favour 1 (leadership), 3 (communication), 8 (commerce) and 9 (reach) for brands. Pair your name with a matching domain and phone number.</p><a class="btn" href="' + ROOT + 'lucky-numbers.html?need=domain">Find a matching numeric domain or phone number</a>' : "");
      } else if (t === "compatibility") {
        var a = v("dob1").split("-"), b = v("dob2").split("-"); if (a.length < 3 || b.length < 3) return;
        var x = E.lifePath(a[0], +a[1], +a[2]).root, y = E.lifePath(b[0], +b[1], +b[2]).root;
        var xr = E.reduce(x, false).root, yr2 = E.reduce(y, false).root;
        var natural = COMPAT[xr].indexOf(yr2) !== -1, verdict = natural ? "Natural match" : (Math.abs(xr - yr2) === 1 ? "Complementary" : "Growth pairing");
        html = '<div class="keys">' + keys(String(x)).replace(/<\/?div[^>]*>/g, "") + '<span class="key sm"><b>+</b></span>' + keys(String(y)).replace(/<\/?div[^>]*>/g, "") + "</div><h3>" + verdict + "</h3><p>Life path " + x + " (" + esc(rootText(x)) + ") with life path " + y + " (" + esc(rootText(y)) + ").</p><p>" +
          (natural ? "Numerology groups 1-5-7, 2-4-8 and 3-6-9 as natural families; you share one, which is read as easy mutual understanding." : "You sit in different number families, which numerologists read as a pairing that grows through difference rather than sameness.") + "</p>";
      } else if (t === "lucky-phone" || t === "lucky-plate" || t === "lucky-address") {
        var raw = v("value"), digits = E.clean(raw);
        if (t === "lucky-plate") { digits = raw.toLowerCase().replace(/[^a-z0-9]/g, "").split("").map(function (c) { return /\d/.test(c) ? c : String(((c.charCodeAt(0) - 97) % 9) + 1); }).join("").slice(0, 15); }
        if (!digits) { out.innerHTML = '<p class="note">Enter at least one digit.</p>'; return; }
        var L = E.luck(digits), red = E.reduce(E.digitSum(digits), true);
        html = keys(digits.slice(0, 12)) + '<p class="eq">Digit sum ' + E.digitSum(digits) + " → root <strong>" + red.root + "</strong> (" + esc(rootText(red.root)) + ")</p>" +
          (t === "lucky-address" && digits.indexOf("4") !== -1 ? '<p class="note">Addresses and floors containing 4 can reduce appeal to East Asian buyers. Some agents report renumbering homes for this reason.</p>' : "") +
          luckBlock(L, digits, t === "lucky-phone" ? "phone" : t === "lucky-plate" ? "plate" : "address");
      }
      out.innerHTML = '<div class="panel">' + html + "</div>";
      out.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "nearest" });
    });
  });

  /* Slang filter */
  var sf = $("#slang-filter");
  if (sf) {
    var rows = $$("#slang-table tbody tr");
    var apply = function () {
      var q = sf.value.toLowerCase(), lang = $("#slang-lang").value;
      rows.forEach(function (r) { var t = r.textContent.toLowerCase(); r.hidden = !(t.indexOf(q) !== -1 && (!lang || r.getAttribute("data-lang") === lang)); });
    };
    sf.addEventListener("input", apply); $("#slang-lang").addEventListener("change", apply);
  }

  /* Daily number widget */
  var dn = $("#daily-number");
  if (dn) {
    var d = new Date(), s = (d.getFullYear() * 10000 + (d.getMonth() + 1) * 100 + d.getDate()), u = E.reduce(E.digitSum(String(s)), true).root;
    dn.innerHTML = keys(String(u)) + '<p class="eq">Today\'s universal day number: <strong>' + u + "</strong></p><p class=\"mt0\">" + esc(rootText(u)) + '.</p>';
  }
  var y = $("[data-year]"); if (y) y.textContent = new Date().getFullYear();
})();
