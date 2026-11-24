# DiSPatch, issue 2. Text from DiSPatch-Issue-02-draft-2 (Amal and Aayush, with review fixes).
# Each story: tag, headline, what happened, why it matters, an optional note, sources.
# Pictures for this issue live in dispatch/issue-02/images/.
# Before sending: confirm Nvidia's 23 Nov close ("about a third"), that India's AI rules paper is still unpublished,
# and the latest on the Riemann claim (still unconfirmed? any errors found?).

NEWSLETTER = 'dispatch'

ISSUE = {'number': 2,
 'volume': 1,
 'date_label': '26 November 2026',
 'date_short': '26 NOV 2026',
 'period': 'fortnight',
 'stamp': None,
 'launch_intro': False,
 'title': 'The fortnight in AI: money, maths, rules and your next job',
 'page_meta': 'A six-minute read, compiled by Amal Francis and Aayush Kalia.',
 'cover': 'images/cover-3.jpg',
 'cover_alt': 'A neon steel rollercoaster whose track drops steeply and then climbs like a stock chart, with a '
              'three-car train of four riders each, carrying a chip, a bell and a padlock, the Analytics Club logo on '
              'the station tower, and a person drawn in glowing lines watching from a railing',
 'cover_bg': '#0B1530',
 'subject': 'DiSPatch #2: A $1M maths proof, AI courts and a CEO U-turn',
 'preheader': 'Plus Nvidia’s boss is back, Anthropic’s record IPO, a ₹65 crore loan hack and fewer fresher jobs.',
 'email_kicker': 'This fortnight’s AI news, about a six-minute read.',
 'email_headline': 'AI may have helped crack maths’ most famous unsolved problem',
 'email_teaser': 'Also in this issue: Nvidia brings back its CEO after 11 days, OpenAI’s cheaper GPT-6.2, Anthropic’s '
                 'record $93.5 billion listing, a Supreme Court judge’s pitch for 24/7 AI divorce courts, and hackers '
                 'who diverted more than ₹65 crore in approved loans.',
 'try': 'Run an “AI shelf audit”: pick a product category you know well, such as credit cards or running shoes, and '
        'ask ChatGPT, Gemini and Copilot the exact same buyer question. Note which brands each one recommends, in what '
        'order, and which sources it cites.'}

NUMBERS = [('48%', 'drop in Nvidia’s share price from its 6 October record to 20 November'),
 ('17M', 'lines of computer-checkable code in the claimed proof of the Riemann hypothesis'),
 ('$93.5B', 'raised in Anthropic’s record-breaking listing, including extra shares'),
 ('₹65 cr+', 'in approved loans diverted by hackers from at least 12 Indian lenders')]

STORIES = [{'num': '01',
  'tag': 'MARKETS',
  'short': 'Nvidia’s CEO is back after 11 days',
  'headline': 'Nvidia brings back Jensen Huang, 11 days after he quit',
  'body': 'Nvidia’s board unanimously brought back Jensen Huang as chief executive on 23 November, just 11 days after '
          'he quit. He had resigned amid reports about his personal relationships and about whether foreign '
          'intelligence had targeted him. Six days before the reversal, the board’s chair said Huang would not return. '
          'After input from senior US officials, the board concluded his return posed no national-security risk. '
          'President Trump, who had urged the move, called it “correct and proper”.',
  'why': 'Investors call this key-person risk, and the market just put a price on it. Nvidia’s shares jumped by about '
         'a third on the news. Since their 6 October peak they had lost nearly half their value, hit by an AI '
         'sell-off, Huang’s exit and a Reuters report that SEC staff were examining possible accounting problems. The '
         'board’s inquiry is still open.',
  'pic': {'label': 'CHART FOR THIS STORY',
          'desc': 'Nvidia’s share price, October to November 2026',
          'file': 'images/nvidia-chart.jpg',
          'alt': 'Line chart of Nvidia’s closing share price from 1 October to 20 November 2026: a record $239 on 6 '
                 'October, an AI sell-off on 5 November, Huang resigning on 12 November, a 14% fall on 20 November '
                 'after a report of an SEC probe, and a jump of about a third on 23 November when he returned'},
  'sources': [('Nvidia (reinstatement filing)',
               'https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000090/nov23pressrelease.htm'),
              ('Reuters via Yahoo Finance',
               'https://finance.yahoo.com/news/nvidia-reinstates-jensen-huang-ceo-135916841.html'),
              ('Reuters via Investing.com (SEC report)',
               'https://www.investing.com/news/stock-market-news/nvidia-shares-fall-10-as-report-of-sec-accounting-probe-adds-to-pressure-5042464')]},
 {'num': '02',
  'tag': 'SCIENCE',
  'short': 'AI and maths’ $1M problem',
  'headline': 'AI may have helped crack maths’ most famous unsolved problem',
  'body': 'On 20 November, Anthropic mathematician Levent Alpöge said he had used Claude to help prove the Riemann '
          'hypothesis, a 167-year-old problem that carries a $1 million prize. Instead of a traditional paper, he '
          'released the proof as roughly 17 million lines of Lean, a programming language in which a computer checks '
          'every logical step. Early checks have passed. The same day, a Stanford researcher posted a proof done '
          'without AI, which is also still being checked.',
  'why': 'If the proof holds up, AI will have helped solve a problem that stumped mathematicians for 167 years, with '
         'an answer no human yet fully understands. Banks already deal with a smaller version of this: risk models '
         'whose outputs can be tested even when their reasoning is hard to explain.',
  'note': 'Mathematicians have not yet accepted the claim. Martin Bridson, head of the Clay Mathematics Institute, '
          'which awards the prize, says real understanding “will be long and difficult”.',
  'sources': [('Alpöge’s announcement (PDF)', 'https://alpo.ge/remark.pdf'),
              ('TechCrunch',
               'https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/'),
              ('AP via 1News',
               'https://www.1news.co.nz/2026/11/23/mathematician-claims-ai-helped-solve-167-year-old-maths-problem/'),
              ('IBM Think', 'https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof')]},
 {'num': '03',
  'tag': 'TOOLS',
  'short': 'New models from OpenAI and Google',
  'headline': 'OpenAI cuts prices with GPT-6.2 as Google launches Gemini 4 Neon',
  'body': 'OpenAI released GPT-6.2 on 17 November in two tiers: Astra, built for heavy lifting, and Sol, a cheaper '
          'option for everyday tasks. For developers, Astra is 20% cheaper than GPT-6 Astra. A day later, Google '
          'unveiled Gemini 4 Neon, which slots between its most powerful model and its fastest one. Google says Neon '
          'tops Artificial Analysis’s index of AI coding agents.',
  'why': 'Top models keep getting cheaper for the same work, so a company choosing AI tools should compare what a '
         'finished task costs as well as where a model ranks.',
  'pic': {'label': 'PICTURE FOR THIS STORY',
          'desc': 'Meme: ordering an AI model',
          'file': 'images/meme-model-menu.jpg',
          'alt': 'Meme captioned “Ordering an AI model in November 2026”: a puzzled robot at a café counter looks up '
                 'at a menu of five glowing items labelled Astra, Sol, Neon, Carbon and Hydrogen'},
  'sources': [('OpenAI', 'https://openai.com/index/introducing-gpt-6-2-astra-sol/'),
              ('Google',
               'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/'),
              ('WinBuzzer',
               'https://winbuzzer.com/2026/11/17/gpt-6-2-scores-higher-at-lower-cost-in-ai-tests-xcxwbn/')]},
 {'num': '04',
  'tag': 'FINANCE',
  'short': 'Anthropic’s record listing',
  'headline': 'Anthropic completes the largest stock-market listing ever',
  'body': 'Anthropic, the maker of Claude, priced its shares at $83 on 18 November, above the range it had set. '
          'Including extra shares bought by its underwriters, the listing raised $93.5 billion, beating SpaceX’s June '
          'listing as the largest ever, and valued Anthropic at about $1.5 trillion. Its shares began trading on '
          'Nasdaq the next day.',
  'why': 'It is the first of the big US AI labs to go public, so investors can now price one every trading day. The '
         'swings started on day one: the shares opened 34% above the offer price and closed 17% up.',
  'sources': [('Anthropic', 'https://www.anthropic.com/news/anthropic-prices-initial-public-offering'),
              ('AP via PBS',
               'https://www.pbs.org/newshour/economy/anthropic-prices-its-ipo-at-83-per-share-valuing-the-ai-giant-at-1-5-trillion'),
              ('Unite.ai ($93.5B close)',
               'https://www.unite.ai/anthropic-closes-enlarged-93-5b-ipo-and-26b-private-placement/'),
              ('TechRepublic (opening price)',
               'https://www.techrepublic.com/article/news-anthropic-ipo-nasdaq-trading-debut/'),
              ('CNN', 'https://www.cnn.com/2026/11/19/business/live-news/anthropic-ipo')]},
 {'num': '05',
  'tag': 'REGULATION',
  'short': 'AI labels: Europe and India',
  'headline': 'Europe’s AI-label deadline is 2 December; India’s rule is already live',
  'body': 'By 2 December, AI tools sold in Europe must tag what they make, text included, so that software can tell it '
          'was made by AI. Tools launched after 2 August 2026 have had to do this from the start. The same day, the EU '
          'will ban AI tools that make non-consensual fake intimate images of real people. India has had its own rule '
          'since 20 February: platforms must label realistic AI-made audio, images and video, and add permanent '
          'metadata where feasible.',
  'why': 'Indian firms selling AI tools in Europe now face two overlapping sets of rules. Europe’s target AI makers '
         'and include text; India’s target platforms and cover audio, images and video. A single compliance plan can '
         'handle both.',
  'note': 'India watch: rules for consent managers under the data protection law took effect on 13 November, with most '
          'other obligations starting on 13 May 2027. The AI rules paper that IT Minister Ashwini Vaishnaw promised on '
          '8 October “within a month” has still not been released.',
  'sources': [('EUR-Lex (AI Omnibus)', 'https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng'),
              ('White & Case', 'https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act'),
              ('MediaNama (IT Rules)',
               'https://www.medianama.com/2026/02/223-meity-amendments-it-rules-synthetic-media-deepfakes/'),
              ('Press Information Bureau (consent managers)',
               'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2336151'),
              ('MediaNama (AI rules paper)',
               'https://www.medianama.com/2026/10/223-meity-consultation-paper-ai-regulation/')]},
 {'num': '06',
  'tag': 'LAW',
  'short': '24/7 AI divorce courts?',
  'headline': 'A Supreme Court judge wants 24/7 AI divorce courts',
  'body': 'Speaking in Jabalpur on 21 November, Supreme Court judge Joymalya Bagchi proposed shifting mutual-consent '
          'divorces to “24/7 AI divorce courts”. With more than five crore cases pending in India, he argued, judges '
          'should not spend time on such “non-adjudicatory” work. He also suggested using AI to predict likely '
          'verdicts in cheque-bounce and money-recovery disputes before arguments begin, while insisting that '
          'constitutional cases stay in human hands.',
  'why': 'In September, the Supreme Court threw out a ₹425 crore customs penalty because the order cited non-existent '
         'judgments, apparently invented by AI, and warned that AI can serve as “training wheels” but not as the '
         'pilot.',
  'pic': {'label': 'PICTURE FOR THIS STORY',
          'desc': 'A robot judge on the night shift',
          'file': 'images/ai-court.jpg',
          'alt': 'Illustration captioned “Court open 24/7”: a small robot in a judge’s robe and collar bands sits at a '
                 'bench at night, tapping a gavel, with case files, a glass of chai, two rings on a tray and a moon '
                 'outside the window'},
  'sources': [('Bar & Bench',
               'https://www.barandbench.com/news/supreme-court-justice-joymalya-bagchi-bats-for-dedicated-ai-courts-to-decide-mutual-consent-divorce-cases'),
              ('The Week',
               'https://www.theweek.in/news/india/2026/11/21/ai-divorce-courts-proposed-supreme-court-judge.html'),
              ('LiveLaw (₹425 crore penalty)',
               'https://www.livelaw.in/supreme-court/supreme-court-sets-aside-425-crore-penalty-as-customs-authority-used-ai-generated-fake-case-laws-548329')]},
 {'num': '07',
  'tag': 'HEALTHCARE',
  'short': 'AI speeds up drug discovery',
  'headline': 'Big drugmakers say AI has cut drug discovery time by up to half',
  'body': 'Scientists at AstraZeneca, Novartis, Sanofi, Novo Nordisk and other big drugmakers told Reuters on 20 '
          'November that AI has cut the time needed to design new molecules and move them into clinical trials by up '
          'to half this year. Novartis said its average time from project start to drug candidate has shrunk from '
          'about three years to 18 to 24 months, and Sanofi said it saved at least a year on an asthma drug.',
  'why': 'Faster, cheaper early research could change how drugmakers and investors value drug pipelines. But these '
         'figures are the companies’ own, and historically nearly nine in ten drugs that enter clinical trials fail, '
         'so quicker discovery does not automatically mean more approved medicines.',
  'sources': [('Reuters via Investing.com',
               'https://www.investing.com/news/stock-market-news/big-pharma-with-eye-on-anthropic-says-ai-is-shrinking-drug-discovery-timelines-5041287'),
              ('STAT',
               'https://www.statnews.com/pharmalot/2026/11/20/sanofi-eyeing-insmed-ai-speeding-drug-development/')]},
 {'num': '08',
  'tag': 'SECURITY',
  'short': 'Attacks on Indian lenders',
  'headline': 'Attackers target Indian payment systems and lenders',
  'body': 'On 20 November, India’s cybersecurity agency CERT-In warned that attackers were altering payment records '
          'and approval chains at firms that handle government-linked payments and vendor payouts, and flagged AI '
          'tools that scan for weak spots. Separately, Delhi Police said hackers had diverted more than ₹65 crore in '
          'approved loans from at least 12 non-banking lenders, and investigators found traces of AI use. It follows '
          'the AI agents we reported in Issue 1, which read data inside Indian organisations without anyone noticing.',
  'why': 'Fraud is shifting from tricking customers to tampering with the systems that approve payments. That makes '
         'approval steps and vendor access a business problem as much as an IT one.',
  'sources': [('WION (CERT-In)',
               'https://www.wionews.com/technology/ai-agents-now-being-used-by-hackers-to-steal-money-cert-in-issues-warning-1795245429991'),
              ('MediaNama', 'https://www.medianama.com/2026/11/223-ai-hackers-approved-loans-nbfc/'),
              ('Outlook India',
               'https://www.outlookindia.com/national/delhi-ncr-nbfc-cyber-fraud-hackers-rs-65-crore-loan-scam'),
              ('DiSPatch Issue 1', 'https://analyticsclub-spjimr.github.io/newsletters/dispatch/issue-01/')]},
 {'num': '09',
  'tag': 'START-UPS',
  'short': 'Sarvam’s rupee-priced AI',
  'headline': 'Sarvam sells India-hosted AI, priced in rupees',
  'body': 'On 16 November, Bengaluru-based Sarvam AI launched Token Factory, a service that runs AI models on '
          'processors in India and bills in rupees. Alongside Sarvam’s own 105-billion-parameter model, it hosts open '
          'models such as DeepSeek, Kimi, GLM and Gemma; DeepSeek V4.1 Flash launched at ₹14 per million input tokens. '
          'When critics asked why a start-up backed by the IndiaAI Mission was serving mostly Chinese models, '
          'co-founder Pratyush Kumar said the service runs on processors Sarvam bought itself, not on subsidised '
          'government computing.',
  'why': 'Local hosting and rupee billing solve two big headaches for Indian businesses. Because most of the models on '
         'offer are Chinese, though, buyers in sensitive sectors will still have to decide whether they are '
         'comfortable using them.',
  'sources': [('Sarvam AI', 'https://www.sarvam.ai/blogs/sarvam-token-factory'),
              ('The Tribune (ANI)',
               'https://www.tribuneindia.com/news/ai-models/no-government-support-for-running-open-weight-ai-models-says-sarvams-co-founder-amid-chinese-models-row'),
              ('MediaNama', 'https://www.medianama.com/2026/11/223-sarvam-token-factory-india-sovereign-ai/')]},
 {'num': '10',
  'tag': 'CAREERS',
  'short': 'Freshers and AI in Indian IT',
  'headline': 'AI isn’t wiping out India’s IT jobs, but freshers are feeling it',
  'body': 'Fears that AI will hollow out India’s outsourcing industry the way Chinese factories hit Western '
          'manufacturing are “overdone”, says a Deutsche Bank report released on 19 November. Staffing firm Xpheno '
          'counted 130,000 tech job openings in November, up 27% on a year earlier. Yet fresher hiring is slowing, and '
          'TCS has 23,460 fewer employees than a year ago. In the US, Goldman Sachs says the feared wave of AI layoffs '
          'did not arrive this year.',
  'why': 'For MBA graduates, the bigger risk is a tighter pool of entry-level roles. Deutsche Bank also warns that '
         'companies pausing junior hiring today could face a shortage of senior talent later.',
  'sources': [('ThePrint (Deutsche Bank report)',
               'https://theprint.in/tech/ai-can-trigger-a-china-shock-for-indias-it-sector-but-deutsche-bank-sees-a-silver-lining/3106745/'),
              ('Fortune (Goldman Sachs)',
               'https://fortune.com/2026/11/16/why-no-ai-layoff-wave-goldman-sachs-outlook-recession-jobs/')]},
 {'num': '11',
  'tag': 'MARKETING',
  'short': 'Do AI-made ads work?',
  'headline': 'AI-made ads look cheap to many Indians, but they still win clicks',
  'body': 'In an Accenture survey released on 18 November, 56% of Indian respondents said brands that use AI for '
          'content or ads look “lazy, careless and cheap”, but the click data says otherwise. A Taboola study with '
          'Columbia and Harvard researchers, covering 500 million ad views, found that AI ads did as well as '
          'human-made ones, and the AI ads that looked most natural drew the most clicks. In a live Instagram test, AI '
          'images even drew about 50% more clicks than images by a professional designer.',
  'why': 'Polished AI ads hold their own, while obviously artificial ones lose clicks. From 29 December, the '
         'Advertising Standards Council of India also requires labels on AI-made ads that could mislead viewers.',
  'pic': {'label': 'PICTURE FOR THIS STORY',
          'desc': 'Meme: the brand’s AI ad, up close',
          'file': 'images/meme-ai-ads.jpg',
          'alt': 'Two-panel meme. Left, captioned “The brand: Our AI ad looks premium”, a small robot proudly shows a '
                 'glossy perfume ad. Right, captioned “56% of Indians surveyed: Lazy, careless and cheap”, a '
                 'magnifying glass shows the hand in the ad has too many fingers and the label is a blob, and the '
                 'robot looks embarrassed'},
  'sources': [('The Tribune (ANI)',
               'https://www.tribuneindia.com/news/accenture-report/ai-in-ads-and-content-makes-brands-look-careless-say-56-of-india-respondents-accenture'),
              ('Accenture',
               'https://newsroom.accenture.com/news/2026/accenture-life-trends-2027-finds-people-want-progress-in-an-ai-era-but-on-their-own-terms'),
              ('Taboola study', 'https://www.taboola.com/press-releases/genai-ads-study-2026/'),
              ('Marketing Science (INFORMS)',
               'https://www.informs.org/News-Room/INFORMS-Releases/News-Releases/AI-Generated-Ads-Outperform-Human-Designers-in-Live-Campaign-Advantage-Holds-18-Months-Later'),
              ('Business Standard (ASCI)',
               'https://www.business-standard.com/amp/industry/news/asci-issues-guidelines-for-labelling-synthetically-generated-content-in-ads-126093000414_1.html')]}]
