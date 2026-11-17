# Analytics Club newsletters

DiSPatch, PerSPective and GraSP from the Analytics Club, SPJIMR. Every issue has its own folder, and GitHub Pages hosts them all.

## What's where

```
index.html                  front page listing every issue
assets/                     club logo, favicon and analytics.js (visitor counting), shared by all issues
dispatch/
  index.html                sends visitors to the DiSPatch list on the front page
  issue-01/
    index.html              the full issue (where "Read the full issue" goes)
    email.html              the email to send
    images/                 cover and story pictures for this issue only
_build/                     the tool that makes the pages (not published)
  config.py                 club details, social links, newsletter names and taglines
  issues/dispatch-01.py     the words of DiSPatch issue 1
  build.py                  turns the issue files into index.html and email.html
_tools/send-email.gs        optional Google Apps Script sender (not published)
```

Folders starting with `_` are not published by GitHub Pages, so the build tool and the sender stay private to the repo.

Issues are numbered rather than dated, so nothing breaks if the schedule moves from fortnightly to weekly or monthly.

## Publishing

1. Create a repository, for example `newsletters`, and upload everything in this folder.
2. Go to Settings → Pages. Under "Build and deployment", choose "Deploy from a branch", then `main` and `/ (root)`.
3. After a minute or two the site is live at `https://analyticsclub-spjimr.github.io/newsletters/`.

Links for issue 1:
- Full issue: `https://analyticsclub-spjimr.github.io/newsletters/dispatch/issue-01/`
- Email: `https://analyticsclub-spjimr.github.io/newsletters/dispatch/issue-01/email.html`

Once you know the address, put it in `SITE_URL` in `_build/config.py` and run the build again. WhatsApp and LinkedIn will then show the cover when someone shares an issue link.

## Sending an issue

**Copy and paste (simplest).** Open the issue's `email.html` link in Chrome, press Ctrl+Shift+R, then Ctrl+A and Ctrl+C, and paste into a new Gmail message. Use the web address, not the file on your computer, so the pictures load for readers.

**Apps Script (pictures show instantly).** Follow the steps at the top of `_tools/send-email.gs`. For each new issue, change only `ISSUE_URL`. The subject line comes from the issue file.

Always send a test to yourself and check it on a phone first.

## Making the next issue

1. Copy `_build/issues/dispatch-01.py` to `_build/issues/dispatch-02.py` and change `number` to 2.
2. Change the date, the stories, the numbers and the email text. Set `stamp` to `None` and `launch_intro` to `False`, because those are only for the first issue.
3. Make the folder `dispatch/issue-02/images/` and put the cover and story pictures in it. Use the file names given in the issue file.
4. Run `python3 _build/build.py` from the repo folder. This creates `dispatch/issue-02/index.html` and `email.html` and adds the issue to the front page.
5. Upload the changes, check the links on your phone, then send.

`python3 _build/build.py` rebuilds every issue, so a design change shows up on old issues too. To rebuild only one issue, name it: `python3 _build/build.py dispatch-02`.

If the schedule changes, update `period` in the issue file ('week', 'fortnight' or 'month') and the `tagline` and `about` lines in `_build/config.py`.

## Analytics (who reads, listens and how far)

Counting is done with [GoatCounter](https://www.goatcounter.com): free for non-commercial sites, no cookies, nothing personal stored, and no backend for us to run. All the counting code is in `assets/analytics.js` and works for every issue automatically.

**Switching it on (once, about 5 minutes)**
1. Sign up at goatcounter.com and choose a code, for example `analyticsclub-spjimr`. Your dashboard will be at `https://analyticsclub-spjimr.goatcounter.com`.
2. On GitHub, open `assets/analytics.js`, click the pencil icon, put your code between the quotes in `var GOATCOUNTER_CODE = '';`, and commit.
3. Open an issue page. The visit shows up on the dashboard within a minute.

To stop your own visits being counted, open the site once on each of your devices with `#toggle-goatcounter` at the end of the address, then reload.

**What you'll see on the dashboard**

| Name on the dashboard | What it counts |
|---|---|
| `/newsletters/dispatch/issue-01/` | Visits to the issue page |
| `/newsletters/` | Visits to the front page |
| `dispatch-01 · Listen: whole issue` | Presses on "Listen to this issue" |
| `dispatch-01 · Listen: story 03` | Presses on one story's Listen button |
| `dispatch-01 · Listen finished: whole issue` | Times the voice read all the way to the end |
| `dispatch-01 · Read 25%` … `Read 100%` | Visits where at least that much of the nine stories came onto the screen. Counted once per visit. |
| `dispatch-01 · Stayed 30 sec+` … `Stayed 6 min+` | Visits that spent at least that long reading. Only time with the page on screen and the reader active in the last 2 minutes (or the Listen voice playing) counts, so a tab left open in the background doesn't add up. |

Example: 300 visits, `Read 50%` = 180 and `Stayed 3 min+` = 90 means 60% of visitors got through at least half the stories, and 30% spent three minutes or more.

Ad blockers stop some counting, so the real numbers are a little higher than the dashboard shows. Emails aren't counted, only the web pages.

## Good to know

- Each issue has its own `images` folder, so a new cover never clashes with an old one and browsers never show a stale picture.
- DiSPatch uses the stories layout (`STORIES` in its issue file). PerSPective uses the single-article layout (`BODY` in its issue file, see `_build/issues/perspective-01.py`) and a blue colour theme set in `config.py`. GraSP's design will be added before it launches.
- To build one issue without touching the others, name it, e.g. `python3 _build/build.py perspective-02`. Avoid rebuilding DiSPatch issue 1 without a reason: its launch email lists the other newsletters as they were on launch day.
- Python 3 is the only thing the build needs. It is already installed on most Macs, and is a free download for Windows.
