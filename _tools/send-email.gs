/**
 * Newsletter sender for Google Apps Script.
 *
 * Why use this instead of copy-paste:
 *  - it sends email.html exactly as built, so it fits phones properly;
 *  - it puts the pictures inside the email, so they show straight away.
 *
 * First time
 * 1. Open script.google.com while signed in to the account that should send the mail.
 * 2. New project. Delete what is there and paste this whole file.
 * 3. Fill in ISSUE_URL and TO_LIST below.
 * 4. Choose sendTest in the toolbar and press Run. Google asks for permission the first time.
 * 5. Open the test mail on your phone and on a laptop. If it looks right, run sendIssue once.
 *
 * Every new issue: change ISSUE_URL only. The subject line is read from the issue's email.html.
 */

const ISSUE_URL = 'https://analyticsclub-spjimr.github.io/newsletters/dispatch/issue-01/'; // the issue's folder, ending with /
const TO_LIST = 'PUT-THE-MAILING-LIST-ADDRESS-HERE';  // fill this in inside Apps Script only, never in the GitHub copy
const FROM_NAME = 'Analytics Club, SPJIMR';

function sendTest() {
  send_(Session.getActiveUser().getEmail());
}

function sendIssue() {
  send_(TO_LIST);
}

function send_(to) {
  const emailUrl = ISSUE_URL + 'email.html';
  let html = UrlFetchApp.fetch(emailUrl).getContentText();

  const found = html.match(/<meta name="subject" content="([^"]*)"/);
  const subject = found ? decode_(found[1]) : 'Analytics Club newsletter';

  // put each picture inside the email
  const inlineImages = {};
  const keys = {};
  html = html.replace(/src="([^"]+)"/g, function (match, src) {
    if (/^(https?:|cid:|data:)/.test(src)) return match;
    const url = resolve_(emailUrl, src);
    if (!keys[url]) {
      keys[url] = 'img' + Object.keys(keys).length;
      inlineImages[keys[url]] = UrlFetchApp.fetch(url).getBlob().setName(url.split('/').pop());
    }
    return 'src="cid:' + keys[url] + '"';
  });

  // links like index.html become full web addresses
  html = html.replace(/href="(?!https?:|mailto:|#)([^"]*)"/g, function (match, href) {
    return 'href="' + resolve_(emailUrl, href) + '"';
  });

  const plain = subject + '\n\nRead it here: ' + ISSUE_URL;
  GmailApp.sendEmail(to, subject, plain, { htmlBody: html, inlineImages: inlineImages, name: FROM_NAME });
}

// Turns a relative path such as ../../assets/logo-mark.png into a full web address.
function resolve_(base, rel) {
  const m = base.match(/^(https?:\/\/[^\/]+)(\/.*)?$/);
  const origin = m[1];
  if (rel.charAt(0) === '/') return origin + rel;
  const dir = (m[2] || '/').replace(/[^\/]*$/, '');
  const out = [];
  (dir + rel).split('/').forEach(function (part) {
    if (part === '..') out.pop();
    else if (part !== '.' && part !== '') out.push(part);
  });
  return origin + '/' + out.join('/') + (/\/$/.test(rel) ? '/' : '');
}

function decode_(s) {
  return s.replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/&#39;/g, "'")
          .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
}
