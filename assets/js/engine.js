/* 55596 number engine — runs entirely in the browser. Requires window.N_DATA (data.js). */
(function (w) {
  "use strict";
  var D = w.N_DATA || {};
  var ONES = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
  var TENS = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];
  var SCALES = ["","thousand","million","billion","trillion"];

  function clean(s) { return String(s || "").replace(/[^0-9]/g, "").slice(0, 15); }
  function digitSum(str) { var t = 0; for (var i = 0; i < str.length; i++) t += +str[i]; return t; }
  function reduce(n, keepMaster) {
    var steps = [n];
    while (n > 9 && !(keepMaster && (n === 11 || n === 22 || n === 33))) {
      n = digitSum(String(n)); steps.push(n);
    }
    return { root: n, steps: steps };
  }

  function words3(n) {
    var out = [];
    if (n >= 100) { out.push(ONES[Math.floor(n / 100)] + " hundred"); n %= 100; }
    if (n >= 20) { out.push(TENS[Math.floor(n / 10)] + (n % 10 ? "-" + ONES[n % 10] : "")); }
    else if (n > 0) out.push(ONES[n]);
    return out.join(" ");
  }
  function toWords(str) {
    var n = Number(str);
    if (!isFinite(n) || str.length > 15) return "";
    if (n === 0) return "zero";
    var parts = [], i = 0;
    while (n > 0 && i < SCALES.length) {
      var chunk = n % 1000;
      if (chunk) parts.unshift(words3(chunk) + (SCALES[i] ? " " + SCALES[i] : ""));
      n = Math.floor(n / 1000); i++;
    }
    return parts.join(" ");
  }
  function toRoman(n) {
    if (n < 1 || n > 3999) return "—";
    var m = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]], r = "";
    m.forEach(function (p) { while (n >= p[0]) { r += p[1]; n -= p[0]; } });
    return r;
  }
  function factorize(n) {
    if (n < 2 || n > 1e13) return null;
    var f = [], d = 2;
    while (n % 2 === 0) { f.push(2); n /= 2; }
    d = 3;
    while (d * d <= n) { while (n % d === 0) { f.push(d); n /= d; } d += 2; }
    if (n > 1) f.push(n);
    return f;
  }
  function factorString(f) {
    var c = {}; f.forEach(function (p) { c[p] = (c[p] || 0) + 1; });
    return Object.keys(c).map(function (p) { return c[p] > 1 ? p + "^" + c[p] : p; }).join(" × ");
  }
  function divisorCount(f) {
    var c = {}; f.forEach(function (p) { c[p] = (c[p] || 0) + 1; });
    return Object.keys(c).reduce(function (a, p) { return a * (c[p] + 1); }, 1);
  }

  function math(str) {
    var n = Number(str), out = { words: toWords(str), roman: toRoman(n), digits: str.length,
      binary: n <= Number.MAX_SAFE_INTEGER ? n.toString(2) : "—",
      octal: n.toString(8), hex: n.toString(16).toUpperCase(),
      palindrome: str.length > 1 && str === str.split("").reverse().join(""),
      even: n % 2 === 0 };
    var sq = Math.sqrt(n); out.square = Number.isInteger(sq) ? sq : null;
    var f = factorize(n);
    if (f) { out.prime = f.length === 1; out.factors = factorString(f); out.divisors = divisorCount(f); }
    return out;
  }

  function isRepeat(str) { return str.length > 1 && /^(\d)\1+$/.test(str); }
  function isSeq(str) {
    if (str.length < 3) return false;
    var up = true, down = true;
    for (var i = 1; i < str.length; i++) {
      if (+str[i] !== (+str[i - 1] + 1) % 10) up = false;
      if (+str[i] !== (+str[i - 1] + 9) % 10) down = false;
    }
    return up || down;
  }
  function isMirror(str) { // 1212, 2323
    return str.length >= 4 && str.length % 2 === 0 && /^(\d\d)\1+$/.test(str);
  }

  function angel(str) {
    var dg = D.digits || {};
    if (isRepeat(str)) {
      return { kind: "Repeating number", text: "Repeated " + str[0] + "s amplify one message: " + dg[str[0]].angel + ". The more repeats, the stronger the signal in angel-number tradition." };
    }
    if (isMirror(str)) {
      return { kind: "Mirror pattern", text: "A repeating pair blends " + dg[str[0]].angel + " with " + dg[str[1]].angel + "." };
    }
    if (isSeq(str)) {
      return { kind: "Sequence", text: "A running sequence is read as steady progress — the next step is already lined up." };
    }
    var counts = {}; str.split("").forEach(function (c) { counts[c] = (counts[c] || 0) + 1; });
    var top = Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; })[0];
    return { kind: "Blended number", text: "The strongest voice is " + top + " (appears " + counts[top] + "×): " + dg[top].angel + ". Read the remaining digits as supporting themes." };
  }

  function combos(str) {
    var hits = [];
    (D.combos || []).forEach(function (c) { if (str.indexOf(c.code) !== -1) hits.push(c); });
    return hits;
  }
  function slang(str) {
    var hits = (D.slang || []).filter(function (s) { return s.code === str; });
    if (!hits.length && /^5{5,}$/.test(str)) hits = (D.slang || []).filter(function (s) { return s.code === "55555"; });
    if (!hits.length && /^23{3,}$/.test(str)) hits = (D.slang || []).filter(function (s) { return s.code === "2333"; });
    if (!hits.length && /^7{3,}$/.test(str)) hits = (D.slang || []).filter(function (s) { return s.code === "7777"; });
    return hits;
  }

  /* Luck score for phone numbers, plates and addresses (Chinese homophone tradition + pattern memorability). */
  var W = { "8": 6, "6": 4, "9": 4, "2": 2, "3": 1, "5": 0, "1": 0, "0": 0, "7": -1, "4": -7 };
  function luck(str) {
    if (!str) return null;
    var s = 50, notes = [];
    var per = 0; for (var i = 0; i < str.length; i++) per += W[str[i]];
    s += Math.round(per * (7 / Math.max(str.length, 7)) * 1.6);
    var fours = (str.match(/4/g) || []).length, eights = (str.match(/8/g) || []).length;
    if (eights) notes.push(eights + "× 8 — 'prosper' (+)");
    if (fours) notes.push(fours + "× 4 — sounds like 'death' in Chinese, Japanese, Korean (−)");
    var last = str[str.length - 1];
    if ("869".indexOf(last) !== -1) { s += 6; notes.push("Ends in " + last + " — a strong lucky ending (+)"); }
    if (last === "4") { s -= 8; notes.push("Ends in 4 — the weakest possible ending (−)"); }
    if (str.indexOf("14") !== -1) { s -= 5; notes.push("Contains 14 — 'yāo sì' ≈ 'want to die' (−)"); }
    if (str.indexOf("250") !== -1) { s -= 4; notes.push("Contains 250 — slang for a fool (−)"); }
    ["168", "518", "888", "666", "999", "1314", "520"].forEach(function (c) { if (str.indexOf(c) !== -1) { s += 5; notes.push("Contains " + c + " — a celebrated combination (+)"); } });
    var runs = str.match(/(\d)\1{2,}/g) || [];
    runs.forEach(function (r) { var b = r[0] === "4" ? -4 : 4 + (r.length - 3) * 2; s += b; notes.push("Run of " + r + (b > 0 ? " — memorable pattern (+)" : " — repeated 4s (−)")); });
    if (isSeq(str)) { s += 4; notes.push("Sequential digits — easy to remember (+)"); }
    s = Math.max(0, Math.min(100, s));
    var grade = s >= 85 ? "Excellent" : s >= 70 ? "Very good" : s >= 55 ? "Good" : s >= 40 ? "Fair" : "Weak";
    return { score: s, grade: grade, notes: notes, better: better(str) };
  }
  function better(str) {
    var out = [];
    if (str.indexOf("4") !== -1) out.push(str.replace(/4/g, "8"));
    if ("869".indexOf(str[str.length - 1]) === -1) out.push(str.slice(0, -1) + "8");
    if (str.length >= 4) out.push(str.slice(0, -3) + "168");
    return out.filter(function (v, i, a) { return v !== str && a.indexOf(v) === i; }).slice(0, 3);
  }

  function decode(input) {
    var str = clean(input);
    if (!str) return null;
    var sum = digitSum(str), red = reduce(sum, true);
    var dg = D.digits || {};
    return {
      str: str, sum: sum, steps: red.steps, root: red.root,
      rootMeaning: (D.master && D.master[String(red.root)]) || (dg[String(red.root)] ? dg[String(red.root)].num : ""),
      digits: str.split("").map(function (c) { return { d: c, letters: (D.keypad || {})[c] || "", zh: dg[c].zh, num: dg[c].num }; }),
      angel: angel(str), combos: combos(str), slang: slang(str), math: math(str), luck: luck(str),
      page: (D.pages || []).indexOf(str) !== -1 ? str : null
    };
  }

  /* Numerology letter tables */
  var PY = {}; "abcdefghijklmnopqrstuvwxyz".split("").forEach(function (c, i) { PY[c] = (i % 9) + 1; });
  var CH = { a:1,i:1,j:1,q:1,y:1,b:2,k:2,r:2,c:3,g:3,l:3,s:3,d:4,m:4,t:4,e:5,h:5,n:5,x:5,u:6,v:6,w:6,o:7,z:7,f:8,p:8 };
  function nameNumber(name, system) {
    var map = system === "chaldean" ? CH : PY, all = 0, vow = 0, con = 0;
    String(name || "").toLowerCase().replace(/[^a-z]/g, "").split("").forEach(function (c) {
      var v = map[c] || 0; all += v; if ("aeiou".indexOf(c) !== -1) vow += v; else con += v;
    });
    return { total: all, expression: reduce(all, true).root, soul: reduce(vow, true).root, personality: reduce(con, true).root };
  }
  function lifePath(y, m, d) {
    var a = reduce(digitSum(String(m)), true).root, b = reduce(digitSum(String(d)), true).root, c = reduce(digitSum(String(y)), true).root;
    var r = reduce(a + b + c, true);
    return { parts: [a, b, c], total: a + b + c, root: r.root };
  }
  function personalYear(m, d, year) {
    return reduce(digitSum(String(m)) + digitSum(String(d)) + digitSum(String(year)), false).root;
  }

  w.N55596 = { clean: clean, reduce: reduce, digitSum: digitSum, decode: decode, luck: luck, math: math, nameNumber: nameNumber, lifePath: lifePath, personalYear: personalYear, toWords: toWords };
})(window);
