"""Builds the Analytics Club newsletter site from the files in _build/.

    python3 _build/build.py               rebuilds every issue and the front page
    python3 _build/build.py dispatch-02   rebuilds only DiSPatch issue 2 (and the front page)

Needs Python 3 and nothing else.
"""
import glob, os, re, runpy, sys
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import config as C  # noqa: E402

INK_RED, INK, MUTED, BODY = '#A82A16', '#14161B', '#6B6F78', '#3B3F48'
MONO = "ui-monospace,'SF Mono',Menlo,Consolas,'Courier New',monospace"
TYPE = "'Courier New',Courier,monospace"
SERIF = "Georgia,'Times New Roman',serif"
WORD = "'Exo 2','Helvetica Neue',Helvetica,Arial,sans-serif"
SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"
FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@700&amp;display=swap" rel="stylesheet">'


def e(t):
    return escape(t, quote=False)


def a(t):
    return escape(t, quote=True)


def fill(tpl, **kw):
    for k, v in kw.items():
        tpl = tpl.replace('%' + k + '%', v)
    return tpl


def newsletter(nid):
    for n in C.NEWSLETTERS:
        if n['id'] == nid:
            return n
    raise SystemExit(f'Unknown newsletter "{nid}". Add it to NEWSLETTERS in _build/config.py.')


def wordmark(n, color=None):
    x, sp, y = n['parts']
    return f'{e(x)}<span style="color:{color or n["accent"]}">{e(sp)}</span>{e(y)}'


def load_issue(path):
    d = runpy.run_path(path)
    issue = dict(d['ISSUE'])
    issue['newsletter'] = d['NEWSLETTER']
    issue['numbers'] = d.get('NUMBERS', [])
    issue['stories'] = d.get('STORIES', [])
    issue['body'] = d.get('BODY', [])
    issue['slug'] = f'issue-{issue["number"]:02d}'
    issue['key'] = f'{issue["newsletter"]}-{issue["number"]:02d}'
    issue['folder'] = f'{issue["newsletter"]}/{issue["slug"]}'
    return issue


def site_assets(issue):
    """Paths as seen from an issue folder, e.g. dispatch/issue-01/."""
    return {'logo': '../../assets/logo-mark.png', 'favicon': '../../assets/favicon.png', 'analytics': '../../assets/analytics.js',
            'page': 'index.html', 'map': {}}


# ------------------------------------------------------------------ web page styles
PAGE_CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:#F7ECE8}
.pg{background:#F7ECE8;color:%INK%;font-family:%SANS%;line-height:1.5}
.pg a{color:%INK_RED%}
.pg img{display:block;max-width:100%;height:auto}
.wrap{max-width:760px;margin:0 auto;padding:0 24px}
.top{background:#fff;border-bottom:1px solid #ECE4DF}
.top .wrap{max-width:1120px;display:flex;align-items:center;gap:12px;padding-top:12px;padding-bottom:12px}
.logo{position:relative;flex:none;display:inline-block;width:44px;height:44px;border-radius:10px;background:#EFE8F6;overflow:hidden}
.logo .ph{position:absolute;top:0;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:center;font:700 14px/1 %SANS%;letter-spacing:.3px;color:#522381}
.pg .logo img{position:relative;width:44px;height:44px;border-radius:10px}
.club b{display:block;font-size:16px;line-height:1.2}
.club span{display:block;font-size:12px;letter-spacing:2px;color:%MUTED%}
.mast{display:flex;justify-content:space-between;align-items:center;gap:16px;padding-top:34px}
.wordmark{display:block;font-family:%WORD%;font-weight:700;font-size:40px;line-height:1.05;letter-spacing:-.5px}
.wordmark span{color:%ACCENT%}
.tagline{display:block;margin-top:6px;font-size:16px;color:%MUTED%}
.stamp{flex:none;display:inline-block;transform:rotate(-7deg);border:3px double %ACCENT%;border-radius:4px;padding:7px 12px;color:%ACCENT%;font-family:%TYPE%;font-size:14px;font-weight:700;letter-spacing:3px;line-height:1.1;text-align:center}
.dateline{display:flex;justify-content:space-between;gap:12px;margin-top:20px;padding:7px 0;border-top:1px solid %INK%;border-bottom:3px double %INK%;font-family:%SERIF%;font-size:13px;letter-spacing:2px;text-transform:uppercase;color:%INK%}
h1{margin:30px 0 0;font-size:clamp(28px,6.4vw,46px);line-height:1.12;letter-spacing:-.025em}
.meta{margin:12px 0 0;font-size:15px;color:%MUTED%}
.cover{position:relative;margin-top:34px;color:%ACCENT%}
.cover img{width:100%;border-radius:14px}
.c{position:absolute;width:16px;height:16px;border:0 solid currentColor}
.c.tl{top:-8px;left:-8px;border-top-width:2px;border-left-width:2px}
.c.tr{top:-8px;right:-8px;border-top-width:2px;border-right-width:2px}
.c.bl{bottom:-8px;left:-8px;border-bottom-width:2px;border-left-width:2px}
.c.br{bottom:-8px;right:-8px;border-bottom-width:2px;border-right-width:2px}
.mono{font-family:%MONO%;letter-spacing:1px}
.label{font-size:12px;color:%MUTED%}
.numbers{margin-top:34px;background:#fff;border:1px solid #ECE4DF;border-radius:16px;padding:20px 22px}
.numgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:14px}
.num b{display:block;font-size:30px;line-height:1.1;letter-spacing:-.5px;color:%ACCENT%}
.num span{display:block;margin-top:4px;font-size:14px;line-height:1.4;color:#4A4E57}
.toc{margin-top:32px}
.toc ol{list-style:none;margin:10px 0 0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:28px}
.toc a{display:flex;align-items:center;gap:12px;min-height:48px;padding:10px 0;border-top:1px solid #E8DCD5;color:%INK%;text-decoration:none;font-size:16px;font-weight:600}
.n{font-family:%MONO%;font-size:13px;font-weight:400;color:%INK_RED%}
.stories{margin-top:28px;background:#fff;border:1px solid #ECE4DF;border-radius:20px;padding:4px 28px}
article{padding:30px 0;border-bottom:1px solid #EEECE7;scroll-margin-top:12px}
figure{margin:0 0 18px}
figure img{width:100%;border-radius:12px}
.tagrow{display:flex;align-items:center;gap:10px}
.tagrow .n{color:%MUTED%}
.tag{background:#FCEDEA;color:%INK_RED%;border-radius:999px;padding:4px 10px;font-family:%MONO%;font-size:11px;letter-spacing:.8px}
article h2{margin:12px 0 0;font-size:clamp(22px,4.8vw,25px);line-height:1.28;letter-spacing:-.01em}
.body{margin:12px 0 0;font-size:17px;line-height:1.65;color:%BODY%}
.why{margin-top:16px;background:#FAF8F6;border:1px solid #F0E9E5;border-radius:12px;padding:16px 18px}
.why h3{display:flex;align-items:center;gap:6px;margin:0;font-size:14px;color:%INK_RED%}
.dot{flex:none;width:6px;height:6px;border-radius:50%;background:%ACCENT%}
.why p{margin:6px 0 0;font-size:16.5px;line-height:1.6}
.sources{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.sources a{display:inline-flex;align-items:center;gap:4px;min-height:42px;padding:8px 14px;border:1px solid #E4E1DB;border-radius:999px;color:#4A4E57;font-size:14px;text-decoration:none}
.try{margin:28px 0;background:#FCEDEA;border-radius:16px;padding:22px 24px}
.try p{margin:8px 0 0;font-size:17px;line-height:1.6}
.foot{margin-top:44px;background:%INK%;color:#fff}
.foot .wrap{padding-top:36px;padding-bottom:40px}
.foot .big{margin:0;font-size:20px;line-height:1.35;font-weight:700}
.foot p{margin:8px 0 0;font-size:16px;line-height:1.55;color:#C9CCD3}
.follow{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:18px;font-size:15px;color:#A3A7B0}
.follow span{flex-basis:100%}
.follow a{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border:1px solid #3A3D45;border-radius:999px;color:#fff;font-weight:600;text-decoration:none}
.fine{margin-top:22px!important;padding-top:16px;border-top:1px solid #2A2D35;font-size:13px!important;color:#A3A7B0!important}
.listen{display:none;align-items:center;gap:8px;min-height:40px;padding:0 14px;border:1.5px solid %ACCENT%;border-radius:999px;background:#fff;color:%INK_RED%;font:600 14px/1 %SANS%;cursor:pointer}
.can-listen .listen{display:inline-flex}
.listen .ico::before{content:"▶";font-size:11px}
.listen[aria-pressed="true"]{background:%ACCENT%;color:#fff}
.listen[aria-pressed="true"] .ico::before{content:"■";font-size:12px}
.listen-all{margin-top:16px;min-height:46px;padding:0 18px;font-size:15px}
.tagrow .listen{margin-left:auto}
.reading{background:#FFE9A8;border-radius:3px;box-shadow:0 0 0 3px #FFE9A8}
.totop{display:inline-block;margin-top:14px;font-size:15px;font-weight:600;color:#FF8A70;text-decoration:none}
@media (max-width:640px){
  .wrap{padding:0 16px}
  .mast{padding-top:26px}
  .wordmark{font-size:36px}
  .tagline{font-size:16px}
  .stamp{font-size:12px;letter-spacing:2px;padding:6px 9px}
  .dateline{font-size:12px;letter-spacing:1.5px}
  h1{font-size:30px}
  .meta{font-size:16px}
  .cover{margin-top:28px}
  .label{font-size:12px}
  .numbers{padding:18px}
  .numgrid{grid-template-columns:repeat(2,minmax(0,1fr));gap:16px 14px}
  .num b{font-size:28px}
  .num span{font-size:15px}
  .toc ol{grid-template-columns:1fr}
  .toc a{font-size:17px}
  .stories{padding:2px 18px;border-radius:16px}
  article{padding:26px 0}
  .tag{font-size:12px}
  article h2{font-size:23px}
  .body{font-size:18px}
  .why h3{font-size:15px}
  .why p{font-size:17px}
  .sources a{font-size:15px}
  .try{padding:20px}
  .try p{font-size:18px}
  .foot p{font-size:17px}
  .listen{font-size:15px;min-height:44px}
}
"""

HOME_CSS = """
.home-h{margin:40px 0 0;font-size:clamp(28px,6vw,40px);line-height:1.15;letter-spacing:-.02em}
.nl{margin-top:28px;background:#fff;border:1px solid #ECE4DF;border-radius:20px;padding:24px 26px}
.nl-head{display:flex;align-items:center;flex-wrap:wrap;gap:12px}
.nl .wordmark{font-size:32px}
.soon{display:inline-block;border:1px solid #E2DCD6;border-radius:999px;padding:4px 10px;font-size:13px;font-weight:600;color:%MUTED%}
.nl-about{margin:8px 0 0;font-size:17px;line-height:1.55;color:%BODY%}
.issues{list-style:none;margin:16px 0 0;padding:0}
.issues a{display:block;padding:14px 0;border-top:1px solid #EEECE7;color:%INK%;text-decoration:none}
.issues .n{display:block;font-size:12px;letter-spacing:1px}
.issues b{display:block;margin-top:4px;font-size:18px;line-height:1.35}
.issues a:hover b{text-decoration:underline}
@media (max-width:640px){
  .nl{padding:20px 18px;border-radius:16px}
  .nl .wordmark{font-size:30px}
  .issues b{font-size:18px}
}
"""


def page_css(accent):
    return fill(PAGE_CSS, INK=INK, SANS=SANS, INK_RED=INK_RED, MUTED=MUTED, WORD=WORD, ACCENT=accent,
                TYPE=TYPE, SERIF=SERIF, MONO=MONO, BODY=BODY)


def says(text):
    """Wrap each sentence so the read-aloud feature can highlight it."""
    parts = re.split(r'(?<=[.!?”])\s+(?=[A-Z“$₹0-9])', text.strip())
    return ' '.join(f'<span class="say">{e(p)}</span>' for p in parts)


def topbar(A, canvas=False):
    onerr = '' if canvas else ' onerror="this.remove()"'
    logo = (f'<span class="logo"><span class="ph" aria-hidden="true">AIC</span>'
            f'<img src="{A["logo"]}" alt="{e(C.CLUB)} logo" width="44" height="44"{onerr}></span>')
    return f'<header class="top"><div class="wrap">{logo}<div class="club"><b>{e(C.CLUB)}</b><span>{e(C.SCHOOL_SHORT)}</span></div></div></header>'


def follow(ext):
    return (f'<div class="follow"><span>Follow the {e(C.CLUB)}</span><a href="{C.LINKEDIN}"{ext}>LinkedIn</a>'
            f'<a href="{C.INSTAGRAM}"{ext}>Instagram</a></div>')


def page_body(issue, A, canvas=False):
    n = newsletter(issue['newsletter'])
    src = lambda p: A['map'].get(p, p)  # noqa: E731
    ext = '' if canvas else ' target="_blank" rel="noopener"'
    period = issue.get('period', 'fortnight')
    nums = ''.join(f'<div class="num"><b>{e(v)}</b><span>{e(t)}</span></div>' for v, t in issue['numbers'])
    toc = ''.join(f'<li><a href="#story-{s["num"]}"><span class="n">{s["num"]}</span>{e(s["short"])}</a></li>' for s in issue['stories'])
    arts = []
    for s in issue['stories']:
        fig = ''
        if 'pic' in s:
            p = src(s['pic']['file'])
            onerr = '' if canvas else ' onerror="this.closest(\'figure\').remove()"'
            fig = (f'<figure><a href="{p}"{ext}><img src="{p}" alt="{a(s["pic"]["alt"])}" width="1600" height="800" '
                   f'loading="lazy"{onerr}></a></figure>')
        srcs = ''.join(f'<a href="{a(u)}"{ext}>{e(name)} <span aria-hidden="true">↗</span></a>' for name, u in s['sources'])
        arts.append(f'''
      <article id="story-{s["num"]}">
        {fig}
        <div class="tagrow"><span class="n">{s["num"]}</span><span class="tag">{e(s["tag"])}</span><button class="listen" type="button" data-target="story-{s["num"]}" data-label="Listen" aria-pressed="false"><span class="ico" aria-hidden="true"></span><span class="lbl">Listen</span></button></div>
        <h2><span class="say">{e(s["headline"])}</span></h2>
        <p class="body">{says(s["body"])}</p>
        <div class="why"><h3 class="say" data-say="Why it matters."><span class="dot"></span>Why it matters</h3><p>{says(s["why"])}</p></div>
        <div class="sources">{srcs}</div>
      </article>''')
    stamp = f'<span class="stamp">{"<br>".join(e(x) for x in issue["stamp"])}</span>' if issue.get('stamp') else ''
    root_cls = 'pg can-listen' if canvas else 'pg'
    return f'''<div class="{root_cls}" id="top">
{topbar(A, canvas)}
<main class="wrap">
  <div class="mast">
    <div><span class="wordmark">{wordmark(n)}</span><span class="tagline">{e(n["tagline"])}</span></div>
    {stamp}
  </div>
  <div class="dateline"><span>Vol. {issue.get("volume", 1)} · No. {issue["number"]}</span><span>{e(issue["date_label"])}</span></div>
  <h1>{e(issue["title"])}</h1>
  <p class="meta">{e(issue["page_meta"])}</p>
  <button class="listen listen-all" type="button" data-label="Listen to this issue" aria-pressed="false"><span class="ico" aria-hidden="true"></span><span class="lbl">Listen to this issue</span></button>
  <div class="cover"><span class="c tl"></span><span class="c tr"></span><span class="c bl"></span><span class="c br"></span><img src="{src(issue["cover"])}" alt="{a(issue["cover_alt"])}" width="1200" height="800"></div>
  <section class="numbers" aria-label="The {e(period)} in numbers"><div class="mono label">THE {e(period.upper())} IN NUMBERS</div><div class="numgrid">{nums}</div></section>
  <nav class="toc" aria-label="In this issue"><div class="mono label">IN THIS ISSUE</div><ol>{toc}<li><a href="#try"><span class="n">+</span>Try this {e(period)}</a></li></ol></nav>
  <div class="stories">{''.join(arts)}
    <div class="try" id="try"><div class="mono label say" data-say="Try this {e(period)}." style="color:{INK_RED}">TRY THIS {e(period.upper())}</div><p>{says(issue["try"])}</p></div>
  </div>
</main>
<footer class="foot"><div class="wrap">
  <p class="big">Spotted a story we missed?</p>
  <p>Reply to the {e(n["name"])} mail and tell us.</p>
  {follow(ext)}
  <p class="fine">{e(n["name"])} is put together by the {e(C.CLUB)}, {e(C.SCHOOL_FULL)}.</p>
  <a class="totop" href="#top">Back to top ↑</a>
</div></footer>
</div>'''


LISTEN_JS = """
(function () {
  var synth = window.speechSynthesis;
  if (!synth || typeof SpeechSynthesisUtterance === 'undefined') return;
  document.documentElement.classList.add('can-listen');
  var voice = null;
  function pickVoice() {
    var vs = synth.getVoices(), pref = ['en-IN', 'en-GB', 'en-US', 'en'];
    for (var i = 0; i < pref.length; i++) for (var j = 0; j < vs.length; j++)
      if ((vs[j].lang || '').replace('_', '-').indexOf(pref[i]) === 0) { voice = vs[j]; return; }
  }
  pickVoice();
  if ('onvoiceschanged' in synth) synth.onvoiceschanged = pickVoice;
  var queue = [], idx = 0, active = null, run = 0, what = 'all';
  function tell(name) { try { document.dispatchEvent(new CustomEvent(name, { detail: { what: what } })); } catch (e) {} }
  function clear() { var r = document.querySelectorAll('.reading'); for (var i = 0; i < r.length; i++) r[i].classList.remove('reading'); }
  function label(btn, on) { btn.setAttribute('aria-pressed', on ? 'true' : 'false'); btn.querySelector('.lbl').textContent = on ? 'Stop' : btn.getAttribute('data-label'); }
  function stop() { run++; synth.cancel(); clear(); if (active) { label(active, false); active = null; } }
  function next(my) {
    if (my !== run) return;
    clear();
    if (idx >= queue.length) { tell('ac:listen-done'); stop(); return; }
    var el = queue[idx++], box = el.getBoundingClientRect();
    el.classList.add('reading');
    if (box.top < 60 || box.bottom > window.innerHeight - 60) el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    var u = new SpeechSynthesisUtterance(el.getAttribute('data-say') || el.textContent);
    if (voice) { u.voice = voice; u.lang = voice.lang; } else { u.lang = 'en-IN'; }
    u.rate = 1;
    u.onend = function () { next(my); };
    u.onerror = function () { next(my); };
    synth.speak(u);
  }
  document.addEventListener('click', function (ev) {
    var btn = ev.target.closest && ev.target.closest('.listen');
    if (!btn) return;
    var again = active === btn;
    stop();
    if (again) return;
    var t = btn.getAttribute('data-target');
    var scope = t ? document.getElementById(t) : document.querySelector('.stories');
    queue = Array.prototype.slice.call(scope.querySelectorAll('.say'));
    idx = 0; active = btn; label(btn, true);
    what = t || 'all'; tell('ac:listen');
    next(run);
  });
  window.addEventListener('pagehide', function () { synth.cancel(); });
})();
"""


def share_tags(issue):
    if not C.SITE_URL:
        return ''
    base = C.SITE_URL.rstrip('/') + '/' + issue['folder'] + '/'
    return (f'\n<meta property="og:url" content="{a(base)}">'
            f'\n<meta property="og:image" content="{a(base + issue["cover"])}">'
            f'\n<meta name="twitter:card" content="summary_large_image">')


def retheme(text, n):
    """Swap the warm DiSPatch colours for a newsletter's own palette (set in config.py)."""
    for old, new in n.get('theme', {}).items():
        text = text.replace(old, new)
    return text


ARTICLE_CSS = """
.kicker{display:inline-block;margin-top:30px;background:#FCEDEA;color:%INK_RED%;border-radius:999px;padding:5px 12px;font-family:%MONO%;font-size:12px;letter-spacing:1px}
.kicker + h1{margin-top:14px}
.art{padding:14px 32px 10px}
.art .ap{margin:20px 0 0;font-size:18px;line-height:1.7;color:%BODY%}
.art h2{margin:40px 0 0;font-size:clamp(22px,4.8vw,26px);line-height:1.28;letter-spacing:-.01em}
.pull{margin:30px 0 4px;padding:6px 0 6px 22px;border-left:4px solid %ACCENT%}
.pull p{margin:0;font-family:%SERIF%;font-size:clamp(21px,4.6vw,25px);line-height:1.45;font-style:italic;color:%INK%}
.pull cite{display:block;margin-top:10px;font-style:normal;font-size:14px;color:%MUTED%}
.points{margin:24px 0 0}
.point{display:flex;gap:16px;padding:20px 0;border-top:1px solid #EEECE7}
.point:last-child{border-bottom:1px solid #EEECE7}
.pn{flex:none;width:40px;height:40px;border-radius:50%;background:#FCEDEA;color:%INK_RED%;display:flex;align-items:center;justify-content:center;font-family:%MONO%;font-size:14px}
.point h3{margin:6px 0 0;font-size:19px;line-height:1.35}
.point p{margin:8px 0 0;font-size:17px;line-height:1.65;color:%BODY%}
.art figure{margin:30px 0 6px}
.art figcaption{margin-top:10px;font-size:14px;line-height:1.5;color:%MUTED%}
.more{display:inline-flex;align-items:center;gap:6px;margin-top:12px;min-height:42px;padding:8px 14px;border:1px solid #E4E1DB;border-radius:999px;color:#4A4E57!important;font-size:15px;line-height:1.35;text-decoration:none}
.video{margin-top:14px}
.video .frame{position:relative;width:100%;aspect-ratio:16/9;border-radius:12px;overflow:hidden;background:#0B1530}
.video iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
.video figcaption{margin-top:8px;font-size:14px;line-height:1.5;color:%MUTED%}
.video figcaption a{color:%INK_RED%}
.art .end{margin:30px 0 26px;padding:20px 22px;background:#FCEDEA;border-radius:14px;font-size:19px;line-height:1.55;font-weight:600;color:%INK%}
@media (max-width:640px){
  .art{padding:6px 18px 6px}
  .art .ap{font-size:18px}
  .point{gap:12px}
  .pn{width:34px;height:34px;font-size:13px}
  .point p{font-size:18px}
  .art figcaption{font-size:15px}
}
"""


def extra_html(x, ext):
    """A link button or an embedded YouTube video, placed under a point or paragraph."""
    if x[0] == 'link':
        return f'<a class="more" href="{a(x[2])}"{ext}>{e(x[1])} <span aria-hidden="true">↗</span></a>'
    if x[0] == 'video':
        vid, title, caption = x[1], x[2], x[3]
        watch = f'https://www.youtube.com/watch?v={vid}'
        return (f'<figure class="video"><div class="frame"><iframe src="https://www.youtube-nocookie.com/embed/{vid}" title="{a(title)}" loading="lazy" '
                f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
                f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'
                f'<figcaption>{e(caption)} <a href="{watch}"{ext}>Watch on YouTube ↗</a></figcaption></figure>')
    return ''


def article_body(issue, A, canvas=False):
    """Layout for a single long article (PerSPective)."""
    n = newsletter(issue['newsletter'])
    src = lambda p: A['map'].get(p, p)  # noqa: E731
    ext = '' if canvas else ' target="_blank" rel="noopener"'
    out, points = [], []

    def flush():
        if points:
            out.append('<div class="points">' + ''.join(points) + '</div>')
            points.clear()
    for b in issue['body']:
        kind = b[0]
        if kind != 'point':
            flush()
        if kind == 'p':
            out.append(f'<p class="ap">{says(b[1])}</p>')
        elif kind == 'h2':
            out.append(f'<h2><span class="say">{e(b[1])}</span></h2>')
        elif kind == 'quote':
            out.append(f'<blockquote class="pull"><p>{says(b[1])}</p><cite>{e(b[2])}</cite></blockquote>')
        elif kind == 'point':
            extra = ''.join(extra_html(x, ext) for x in (b[4] if len(b) > 4 else []))
            points.append(f'<div class="point"><span class="pn">{e(b[1])}</span><div><h3><span class="say">{e(b[2])}</span></h3><p>{says(b[3])}</p>{extra}</div></div>')
        elif kind in ('video', 'link'):
            out.append(extra_html(b, ext))
        elif kind == 'fig':
            onerr = '' if canvas else ' onerror="this.closest(\'figure\').remove()"'
            cap = f'<figcaption>{e(b[3])}</figcaption>' if len(b) > 3 and b[3] else ''
            out.append(f'<figure><img src="{src(b[1])}" alt="{a(b[2])}" width="1600" height="800" loading="lazy"{onerr}>{cap}</figure>')
        elif kind == 'end':
            out.append(f'<p class="end">{says(b[1])}</p>')
    flush()
    stamp = f'<span class="stamp">{"<br>".join(e(x) for x in issue["stamp"])}</span>' if issue.get('stamp') else ''
    root_cls = 'pg can-listen' if canvas else 'pg'
    return f'''<div class="{root_cls}" id="top">
{topbar(A, canvas)}
<main class="wrap">
  <div class="mast">
    <div><span class="wordmark">{wordmark(n)}</span><span class="tagline">{e(n["tagline"])}</span></div>
    {stamp}
  </div>
  <div class="dateline"><span>Vol. {issue.get("volume", 1)} · No. {issue["number"]}</span><span>{e(issue["date_label"])}</span></div>
  <span class="kicker">{e(issue["kicker"])}</span>
  <h1>{e(issue["title"])}</h1>
  <p class="meta">{e(issue["page_meta"])}</p>
  <button class="listen listen-all" type="button" data-label="Listen to this article" aria-pressed="false"><span class="ico" aria-hidden="true"></span><span class="lbl">Listen to this article</span></button>
  <div class="cover"><span class="c tl"></span><span class="c tr"></span><span class="c bl"></span><span class="c br"></span><img src="{src(issue["cover"])}" alt="{a(issue["cover_alt"])}" width="1200" height="800"></div>
  <div class="stories art">
    {"".join(out)}
  </div>
</main>
<footer class="foot"><div class="wrap">
  <p class="big">{e(issue.get("reply_big", "Spotted a story we missed?"))}</p>
  <p>{e(issue.get("reply_small", "Reply to the " + n["name"] + " mail and tell us."))}</p>
  {follow(ext)}
  <p class="fine">{e(n["name"])} is put together by the {e(C.CLUB)}, {e(C.SCHOOL_FULL)}.</p>
  <a class="totop" href="#top">Back to top ↑</a>
</div></footer>
</div>'''


def page_html(issue):
    n = newsletter(issue['newsletter'])
    A = site_assets(issue)
    return retheme(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(n["name"])} · Issue {issue["number"]} · {e(C.CLUB)}, {e(C.SCHOOL_SHORT)}</title>
<meta name="description" content="{a(issue["title"])}. {a(n["name"])} from the {a(C.CLUB)}, {a(C.SCHOOL_SHORT)}.">
<meta property="og:title" content="{a(n["name"])} · Issue {issue["number"]}">
<meta property="og:description" content="{a(issue["title"])}.">{share_tags(issue)}
<meta name="theme-color" content="#F7ECE8">
<meta name="color-scheme" content="light">
<link rel="icon" type="image/png" href="{A["favicon"]}">
<link rel="apple-touch-icon" href="{A["logo"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONT_LINK}
<style>{page_css(n["accent"])}{fill(ARTICLE_CSS, INK_RED=INK_RED, MONO=MONO, ACCENT=n["accent"], SERIF=SERIF, INK=INK, MUTED=MUTED, BODY=BODY) if issue['body'] else ''}</style>
<script src="{A["analytics"]}" defer></script>
</head>
<body>
{article_body(issue, A) if issue['body'] else page_body(issue, A)}
<script>{LISTEN_JS}</script>
</body>
</html>
''', n)


# ------------------------------------------------------------------ email
def launch_intro(issue):
    def row(n, first):
        pill = ('' if n['status'] == 'live' else
                '&nbsp;&nbsp;<span style="display:inline-block;font-family:Arial,sans-serif;font-size:12px;line-height:14px;font-weight:bold;'
                'color:#6B6F78;border:1px solid #E2DCD6;border-radius:999px;padding:3px 9px;vertical-align:middle;">Coming soon</span>')
        desc = n['about'] + (' You’re reading the first one.' if first else '')
        return (f'<tr><td style="padding:12px 0;border-top:1px solid #F0DCD5;">'
                f'<div style="font-family:{WORD};font-size:18px;line-height:23px;font-weight:bold;color:{INK};">{wordmark(n)}{pill}</div>'
                f'<div style="padding-top:3px;font-family:{SANS};font-size:16px;line-height:24px;color:#4A4E57;">{e(desc)}</div></td></tr>')

    rows = ''.join(row(n, n['id'] == issue['newsletter']) for n in C.NEWSLETTERS)
    return f'''
<tr><td class="px" style="padding:24px 24px 0 24px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FDF5F2" style="background-color:#FDF5F2;border:1px solid #F2DDD6;border-radius:14px;">
  <tr><td style="padding:20px 20px 8px 20px;">
    <p style="margin:0;font-family:{SANS};font-size:18px;line-height:25px;font-weight:bold;color:{INK};">Hi everyone,</p>
    <p style="margin:10px 0 12px 0;font-family:{SANS};font-size:17px;line-height:26px;color:{BODY};">This is the {e(C.CLUB)}! We’re starting a set of newsletters so that all of us can keep up with AI without having to chase it ourselves. There’ll be three:</p>
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}
      <tr><td style="padding:12px 0 10px 0;border-top:1px solid #F0DCD5;font-family:{SANS};font-size:17px;line-height:26px;color:{BODY};">Have a read, and let us know what you think. Just reply to this mail.</td></tr>
    </table>
  </td></tr></table>
</td></tr>
'''


def email_inner(issue, A):
    n = newsletter(issue['newsletter'])
    src = lambda p: A['map'].get(p, p)  # noqa: E731
    page_url = A['page']
    accent = n['accent']
    pill = ('display:inline-block;font-family:Arial,sans-serif;font-size:15px;line-height:18px;font-weight:bold;color:#FFFFFF;'
            'text-decoration:none;border:1px solid #3A3D45;border-radius:999px;padding:10px 18px;')
    intro = launch_intro(issue) if issue.get('launch_intro') else ''
    if issue.get('intro_text'):
        intro = (f'\n<tr><td class="px" style="padding:24px 24px 0 24px;">\n  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FDF5F2" style="background-color:#FDF5F2;border:1px solid #F2DDD6;border-radius:14px;">\n'
                 f'  <tr><td style="padding:18px 20px;">\n    <p style="margin:0;font-family:{SANS};font-size:18px;line-height:25px;font-weight:bold;color:{INK};">Hi everyone,</p>\n'
                 f'    <p style="margin:8px 0 0 0;font-family:{SANS};font-size:17px;line-height:26px;color:{BODY};">{e(issue["intro_text"])}</p>\n  </td></tr></table>\n</td></tr>\n')
    byline = (f'\n  <p style="margin:12px 0 0 0;font-family:{SANS};font-size:15px;line-height:22px;color:{MUTED};">{e(issue["email_byline"])}</p>'
              if issue.get('email_byline') else '')
    button = e(issue.get('button', 'Read the full issue'))
    cover_bg = issue.get('cover_bg', '#F3E6E1')
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F7ECE8" style="background-color:#F7ECE8;">
<tr><td class="outer" align="center" style="padding:20px 10px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="#FFFFFF" style="max-width:600px;margin:0 auto;background-color:#FFFFFF;border:1px solid #E4E1DB;border-radius:20px;">

<tr><td class="px" style="padding:22px 24px 0 24px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td width="44" valign="middle" style="width:44px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td width="44" height="44" align="center" valign="middle" bgcolor="#EFE8F6" style="width:44px;height:44px;background-color:#EFE8F6;border-radius:10px;font-family:Arial,sans-serif;font-size:14px;line-height:44px;font-weight:bold;color:#522381;text-align:center;"><img src="{A["logo"]}" width="44" height="44" alt="AIC" style="display:block;width:44px;height:44px;border:0;border-radius:10px;font-family:Arial,sans-serif;font-size:14px;line-height:44px;font-weight:bold;color:#522381;text-align:center;"></td></tr></table>
    </td>
    <td valign="middle" style="padding-left:10px;font-family:{SANS};white-space:nowrap;">
      <div style="font-size:16px;line-height:20px;font-weight:bold;color:{INK};">{e(C.CLUB)}</div>
      <div style="font-size:12px;line-height:16px;letter-spacing:2px;color:{MUTED};">{e(C.SCHOOL_SHORT)}</div>
    </td>
  </tr></table>
</td></tr>

<tr><td class="px" style="padding:18px 24px 20px 24px;border-bottom:1px solid #EEECE7;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
    <td valign="bottom" style="text-align:left;">
      <div class="wm" style="font-family:{WORD};font-size:44px;line-height:48px;font-weight:bold;color:{INK};letter-spacing:-0.5px;">{wordmark(n)}</div>
      <div style="padding-top:4px;font-family:{SANS};font-size:16px;line-height:22px;color:{MUTED};">{e(n["tagline"])}</div>
    </td>
    <td valign="bottom" align="right" style="padding-bottom:4px;text-align:right;font-family:{TYPE};font-size:12px;line-height:18px;letter-spacing:1px;color:{MUTED};white-space:nowrap;">ISSUE {issue["number"]:02d}<br>{e(issue["date_short"])}</td>
  </tr></table>
</td></tr>
{intro}
<tr><td class="px" style="padding:28px 24px 0 24px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{cover_bg}" style="background-color:{cover_bg};border-radius:12px;">
  <a href="{page_url}" style="display:block;text-decoration:none;"><img src="{src(issue["cover"])}" width="100%" alt="{a(n["name"])}, issue {issue["number"]}" style="display:block;max-width:100%;height:auto;border:0;border-radius:12px;font-family:{SANS};font-size:15px;line-height:22px;color:#F4C7BE;"></a>
  </td></tr></table>
</td></tr>

<tr><td class="px" style="padding:24px 24px 0 24px;">
  <p style="margin:0 0 10px 0;font-family:{SANS};font-size:15px;line-height:22px;color:{MUTED};">{e(issue["email_kicker"])}</p>
  <h2 class="hl" style="margin:0;font-family:{SANS};font-size:28px;line-height:34px;font-weight:bold;color:{INK};letter-spacing:-0.5px;">{e(issue["email_headline"])}</h2>
  <p style="margin:12px 0 0 0;font-family:{SANS};font-size:17px;line-height:27px;color:{BODY};">{e(issue["email_teaser"])}</p>{byline}
</td></tr>

<tr><td class="px btn" style="padding:24px 24px 0 24px;">
  <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{page_url}" style="height:50px;v-text-anchor:middle;width:250px;" arcsize="50%" stroke="f" fillcolor="{accent}"><center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:17px;font-weight:bold;">{button} &rarr;</center></v:roundrect><![endif]-->
  <!--[if !mso]><!--><a href="{page_url}" style="display:inline-block;background-color:{accent};color:#FFFFFF;font-family:{SANS};font-size:17px;line-height:20px;font-weight:bold;text-decoration:none;padding:15px 26px;border-radius:999px;">{button} &rarr;</a><!--<![endif]-->
</td></tr>

<tr><td class="px" style="padding:30px 24px 0 24px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{INK}" style="background-color:{INK};border-radius:16px;">
  <tr><td style="padding:22px 22px;">
    <p style="margin:0;font-family:{SANS};font-size:18px;line-height:25px;font-weight:bold;color:#FFFFFF;">{e(issue.get("reply_big", "Spotted a story we missed?"))}</p>
    <p style="margin:6px 0 0 0;font-family:{SANS};font-size:16px;line-height:24px;color:#C9CCD3;">{e(issue.get("email_reply_small", "Reply to this mail and tell us."))}</p>
    <p style="margin:16px 0 0 0;padding-top:14px;border-top:1px solid #2A2D35;font-family:{SANS};font-size:15px;line-height:20px;color:#A3A7B0;">Follow the {e(C.CLUB)}</p>
    <p style="margin:10px 0 0 0;line-height:46px;"><a href="{C.LINKEDIN}" style="{pill}">LinkedIn</a>&nbsp;&nbsp;<a href="{C.INSTAGRAM}" style="{pill}">Instagram</a></p>
  </td></tr></table>
</td></tr>

<tr><td class="px" style="padding:18px 24px 26px 24px;font-family:{SANS};font-size:13px;line-height:20px;color:{MUTED};">
  <strong style="color:{INK};">{e(n["name"])}</strong> is put together by the {e(C.CLUB)}, {e(C.SCHOOL_FULL)}.
</td></tr>

</table>
</td></tr></table>'''


EMAIL_CSS = """
body{margin:0!important;padding:0!important;width:100%!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}
img{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic}
table{border-collapse:separate}
a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important}
@media only screen and (max-width:480px){
  .outer{padding:10px 6px!important}
  .px{padding-left:18px!important;padding-right:18px!important}
  .wm{font-size:40px!important;line-height:44px!important}
  .hl{font-size:26px!important;line-height:32px!important}
}
"""


def email_html(issue):
    n = newsletter(issue['newsletter'])
    inner = email_inner(issue, site_assets(issue))
    inner = inner.replace('<tr><td class="outer" align="center" style="padding:20px 10px;">\n',
                          '<tr><td class="outer" align="center" style="padding:20px 10px;">\n<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td><![endif]-->\n', 1)
    inner = inner.replace('</table>\n</td></tr></table>', '</table>\n<!--[if mso]></td></tr></table><![endif]-->\n</td></tr></table>', 1)
    return retheme(f'''<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<meta name="subject" content="{a(issue["subject"])}">
<title>{e(n["name"])} · Issue {issue["number"]}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>{EMAIL_CSS}</style>
</head>
<body style="margin:0;padding:0;background-color:#F7ECE8;">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:#F7ECE8;opacity:0;">{e(issue["preheader"])}&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;&#8203;&nbsp;</div>
{inner}
</body>
</html>
''', n)


# ------------------------------------------------------------------ front page
def front_page(issues):
    A = {'logo': 'assets/logo-mark.png', 'favicon': 'assets/favicon.png', 'analytics': 'assets/analytics.js', 'map': {}}
    ext = ' target="_blank" rel="noopener"'
    blocks = []
    for n in C.NEWSLETTERS:
        mine = sorted((i for i in issues if i['newsletter'] == n['id']), key=lambda i: -i['number'])
        if mine:
            items = ''.join(f'<li><a href="{i["folder"]}/"><span class="n mono">ISSUE {i["number"]:02d} · {e(i["date_label"].upper())}</span>'
                            f'<b>{e(i["title"])}</b></a></li>' for i in mine)
            extra, lst = '', f'<ol class="issues">{items}</ol>'
        else:
            extra, lst = '<span class="soon">Coming soon</span>', ''
        blocks.append(f'''
  <section class="nl" id="{n["id"]}">
    <div class="nl-head"><span class="wordmark">{wordmark(n)}</span>{extra}</div>
    <p class="nl-about">{e(n["about"])}</p>
    {lst}
  </section>''')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Newsletters · {e(C.CLUB)}, {e(C.SCHOOL_SHORT)}</title>
<meta name="description" content="Every newsletter issue from the {a(C.CLUB)}, {a(C.SCHOOL_SHORT)}.">
<meta name="theme-color" content="#F7ECE8">
<meta name="color-scheme" content="light">
<link rel="icon" type="image/png" href="{A["favicon"]}">
<link rel="apple-touch-icon" href="{A["logo"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONT_LINK}
<style>{page_css(INK_RED)}{fill(HOME_CSS, MUTED=MUTED, BODY=BODY, INK=INK)}</style>
<script src="{A["analytics"]}" defer></script>
</head>
<body>
<div class="pg" id="top">
{topbar(A)}
<main class="wrap">
  <h1 class="home-h">Newsletters from the {e(C.CLUB)}</h1>
  <p class="meta">Every issue we’ve sent, in one place.</p>{''.join(blocks)}
</main>
<footer class="foot"><div class="wrap">
  {follow(ext)}
  <p class="fine">The {e(C.CLUB)}, {e(C.SCHOOL_FULL)}.</p>
</div></footer>
</div>
</body>
</html>
'''


def redirect_page(target, title):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
</head>
<body><p><a href="{target}">{e(title)}</a></p></body>
</html>
'''


# ------------------------------------------------------------------ run
def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    return path


def all_issues():
    return [load_issue(p) for p in sorted(glob.glob(os.path.join(HERE, 'issues', '*.py')))]


def main(args):
    issues = all_issues()
    wanted = [i for i in issues if not args or i['key'] in args]
    missing = set(args) - {i['key'] for i in issues}
    if missing:
        raise SystemExit('No issue file for: ' + ', '.join(sorted(missing)) + '. Expected _build/issues/<name>.py, e.g. dispatch-02.py')
    for i in wanted:
        if i['newsletter'] == 'grasp':
            raise SystemExit(f'{i["key"]}: the GraSP design is not built yet.')
        cover = os.path.join(ROOT, i['folder'], i['cover'])
        if not os.path.exists(cover):
            print(f'  note: {i["folder"]}/{i["cover"]} is missing. Add the picture before publishing.')
        write(i['folder'] + '/index.html', page_html(i))
        write(i['folder'] + '/email.html', email_html(i))
        print(f'built {i["folder"]}/index.html and email.html')
    write('index.html', front_page(issues))
    for n in C.NEWSLETTERS:
        if any(i['newsletter'] == n['id'] for i in issues):
            write(n['id'] + '/index.html', redirect_page('../#' + n['id'], f'All {n["name"]} issues'))
    print('built index.html (front page)')


if __name__ == '__main__':
    main(sys.argv[1:])
