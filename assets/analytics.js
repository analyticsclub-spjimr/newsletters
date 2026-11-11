/*
 * Visitor counting for the Analytics Club newsletters, using GoatCounter (goatcounter.com).
 * Free for clubs and non-commercial sites. No cookies, and nothing personal is stored.
 *
 * TO SWITCH IT ON: put your GoatCounter code between the quotes below.
 * If your dashboard is https://analyticsclub-spjimr.goatcounter.com, the code is analyticsclub-spjimr.
 * Leave it empty ('') to switch counting off.
 */
var GOATCOUNTER_CODE = 'analyticsclub-spjimr';

(function () {
  if (!GOATCOUNTER_CODE) return;

  // 1. Load GoatCounter. It counts one visit for every page that opens.
  var tag = document.createElement('script');
  tag.async = true;
  tag.src = 'https://gc.zgo.at/count.js';
  tag.setAttribute('data-goatcounter', 'https://' + GOATCOUNTER_CODE + '.goatcounter.com/count');
  document.head.appendChild(tag);

  // The rest only runs on an issue page, such as /dispatch/issue-01/.
  var found = location.pathname.match(/\/([a-z]+)\/issue-(\d+)\//);
  if (!found) return;
  var issue = found[1] + '-' + found[2];   // for example "dispatch-01"

  var waiting = [];
  function send(name) {
    waiting.push({ path: issue + ' · ' + name, title: name, event: true });
    flush();
  }
  function flush() {
    if (!(window.goatcounter && window.goatcounter.count)) return;
    while (waiting.length) window.goatcounter.count(waiting.shift());
  }
  var poll = setInterval(function () { flush(); if (window.goatcounter && window.goatcounter.count) clearInterval(poll); }, 500);

  // 2. Listen button: each press that starts reading, and each time it reads to the end.
  function part(what) { return what === 'all' ? 'whole issue' : 'story ' + what.replace('story-', ''); }
  document.addEventListener('ac:listen', function (ev) { send('Listen: ' + part(ev.detail.what)); });
  document.addEventListener('ac:listen-done', function (ev) { send('Listen finished: ' + part(ev.detail.what)); });

  // 3. How much of the stories came onto the screen: 25%, 50%, 75%, 100%. Each counts once per visit.
  var stories = document.querySelector('.stories') || document.querySelector('main');
  var marks = [25, 50, 75, 100], reached = 0;
  function checkScroll() {
    if (!stories || reached >= marks.length) return;
    var box = stories.getBoundingClientRect();
    var seen = (window.innerHeight - box.top) / box.height * 100;
    while (reached < marks.length && seen + 0.5 >= marks[reached]) send('Read ' + marks[reached++] + '%');
  }
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    setTimeout(function () { ticking = false; checkScroll(); }, 250);
  }, { passive: true });

  // 4. Time actually spent: only seconds when the page is on screen and the reader has
  //    scrolled, tapped or typed in the last 2 minutes, or the Listen voice is playing.
  var lastActive = Date.now();
  ['scroll', 'touchstart', 'mousemove', 'keydown', 'click'].forEach(function (type) {
    window.addEventListener(type, function () { lastActive = Date.now(); }, { passive: true });
  });
  var times = [[30, '30 sec+'], [60, '1 min+'], [180, '3 min+'], [360, '6 min+']], seconds = 0, next = 0;
  var clock = setInterval(function () {
    var listening = !!document.querySelector('.listen[aria-pressed="true"]');
    if (document.visibilityState !== 'visible') return;
    if (!listening && Date.now() - lastActive > 120000) return;
    seconds++;
    while (next < times.length && seconds >= times[next][0]) send('Stayed ' + times[next++][1]);
    if (next >= times.length) clearInterval(clock);
  }, 1000);
})();
