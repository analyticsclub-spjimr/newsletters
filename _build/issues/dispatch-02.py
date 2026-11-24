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
 'title': 'Eleven AI stories on money, maths, rules and your next job',
 'page_meta': 'A seven-minute read, compiled by Amal Francis and Aayush Kalia.',
 'cover': 'images/cover-3.jpg',
 'cover_alt': 'A neon steel rollercoaster whose track drops steeply and then climbs like a stock chart, with a '
              'three-car train of four riders each, carrying a chip, a bell and a padlock, the Analytics Club logo on '
              'the station tower, and a person drawn in glowing lines watching from a railing',
 'cover_bg': '#0B1530',
 'subject': 'DiSPatch #2: A $1M maths proof, AI courts, a CEO U-turn',
 'preheader': 'Plus Nvidia’s boss is back, Anthropic’s record IPO, a ₹65 crore loan hack and fewer fresher jobs.',
 'email_kicker': 'Eleven stories this fortnight, about a seven-minute read.',
 'email_headline': 'AI may have helped crack maths’ most famous unsolved problem',
 'email_teaser': 'Also in this issue: Nvidia takes back its CEO after 11 days, Anthropic’s record $93.5 billion '
                 'listing, a Supreme Court judge’s idea for 24/7 AI divorce courts, and hackers who diverted more than '
                 '₹65 crore of approved loans.',
 'try': 'Run an “AI shelf audit”: pick a product category you know, such as credit cards or running shoes, and ask '
        'ChatGPT, Gemini and Copilot the same buyer question. Note which brands each one recommends, in what order, '
        'and which sources it cites.'}

NUMBERS = [('48%', 'drop in Nvidia’s shares from their 6 October record to 20 November'),
 ('17M', 'lines of computer-checkable code in the claimed Riemann proof'),
 ('$93.5B', 'raised in Anthropic’s record listing, including extra shares'),
 ('₹65 cr+', 'in approved loans diverted from at least 12 Indian lenders')]

STORIES = [{'num': '01',
  'tag': 'MARKETS',
  'short': 'Nvidia’s CEO is back after 11 days',
  'headline': 'Nvidia brings back Jensen Huang, 11 days after he quit',
  'body': 'Nvidia’s board unanimously reinstated Jensen Huang as chief executive on 23 November, 11 days after he '
          'resigned following reports about his personal relationships and whether he had been targeted by foreign '
          'intelligence. Six days earlier, its chair had said Huang would not return. After input from senior US '
          'officials, the board said his return posed no national-security risk. President Trump, who had urged the '
          'move, called it “correct and proper”.',
  'why': 'The shares jumped by about a third, having lost nearly half their value since 6 October as an AI sell-off '
         'met Huang’s exit and a Reuters report that SEC staff were examining possible accounting problems. The '
         'board’s inquiry is still open. This is key-person risk on a trillion-dollar scale.',
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
  'body': 'On 20 November, Levent Alpöge, a mathematician at Anthropic, said he had found a proof of the Riemann '
          'hypothesis with Claude’s help. The 167-year-old problem carries a $1 million prize. Instead of a paper, he '
          'released some 17 million lines of Lean, code that a computer can check step by step, and early checks have '
          'passed. The same day, a Stanford researcher posted an all-human proof, still being checked.',
  'why': 'If it holds, AI will have helped crack a problem that beat mathematicians for 167 years, with a proof no '
         'human yet fully understands. Managers face the same gap at work: answers that can be checked but not '
         'explained.',
  'note': 'Disclosure: Alpöge works at Anthropic, which makes Claude, and this issue was drafted with help from '
          'Claude. Mathematicians have not yet accepted the claim; the head of the Clay Institute, which awards the '
          'prize, says real understanding “will be long and difficult”.',
  'sources': [('Alpöge’s announcement (PDF)', 'https://alpo.ge/remark.pdf'),
              ('TechCrunch',
               'https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/'),
              ('AP via 1News',
               'https://www.1news.co.nz/2026/11/23/mathematician-claims-ai-helped-solve-167-year-old-maths-problem/'),
              ('IBM Think', 'https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof')]},
 {'num': '03',
  'tag': 'FINANCE',
  'short': 'Anthropic’s record listing',
  'headline': 'Anthropic completes the largest stock-market listing ever',
  'body': 'Anthropic, maker of the Claude chatbot, priced its initial public offering at $83 a share on 18 November, '
          'above its $70–78 range. Selling 980 million shares raised about $81.3 billion, beating SpaceX’s June '
          'listing as the largest ever, and the total reached $93.5 billion after underwriters bought 147 million '
          'extra shares. That valued the company at about $1.5 trillion. Its shares began trading on Nasdaq the next '
          'day.',
  'why': 'It is the first of the big US AI labs to list, so investors can now price one every trading day. The first '
         'day showed how jumpy that price can be: the shares opened 34% above the offer price and closed 17% up.',
  'sources': [('Anthropic', 'https://www.anthropic.com/news/anthropic-prices-initial-public-offering'),
              ('AP via PBS',
               'https://www.pbs.org/newshour/economy/anthropic-prices-its-ipo-at-83-per-share-valuing-the-ai-giant-at-1-5-trillion'),
              ('Unite.ai ($93.5B close)',
               'https://www.unite.ai/anthropic-closes-enlarged-93-5b-ipo-and-26b-private-placement/'),
              ('TechRepublic (opening price)',
               'https://www.techrepublic.com/article/news-anthropic-ipo-nasdaq-trading-debut/'),
              ('CNN', 'https://www.cnn.com/2026/11/19/business/live-news/anthropic-ipo')]},
 {'num': '04',
  'tag': 'REGULATION',
  'short': 'AI labels: Europe and India',
  'headline': 'Europe’s AI-label deadline is 2 December; India’s rule is already live',
  'body': 'Under the EU’s AI Act, generative AI tools sold before 2 August 2026 must mark their output, text included, '
          'in a machine-readable way by 2 December; newer tools have had to since launch. The same day, an EU ban on '
          'AI tools that make fake intimate images of real people without consent takes effect. India’s rule, in force '
          'since 20 February, makes platforms label realistic AI-made audio, images and video and, where feasible, add '
          'permanent metadata.',
  'why': 'Indian firms selling AI tools in Europe face two regimes: the EU’s targets AI makers and covers text, while '
         'India’s targets platforms and covers audio and video. One compliance plan should cover both.',
  'note': 'India watch: rules for consent managers under the data protection law took effect on 13 November; most '
          'other duties start on 13 May 2027. The AI rules paper that IT Minister Ashwini Vaishnaw promised on 8 '
          'October “within a month” is still not out.',
  'sources': [('EUR-Lex (AI Omnibus)', 'https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng'),
              ('White & Case', 'https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act'),
              ('MediaNama (IT Rules)',
               'https://www.medianama.com/2026/02/223-meity-amendments-it-rules-synthetic-media-deepfakes/'),
              ('Press Information Bureau (consent managers)',
               'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2336151'),
              ('MediaNama (AI rules paper)',
               'https://www.medianama.com/2026/10/223-meity-consultation-paper-ai-regulation/')]},
 {'num': '05',
  'tag': 'LAW',
  'short': '24/7 AI divorce courts?',
  'headline': 'A Supreme Court judge wants 24/7 AI divorce courts',
  'body': 'Speaking in Jabalpur on 21 November, Supreme Court judge Joymalya Bagchi proposed moving mutual-consent '
          'divorces to “24/7 AI divorce courts”, so judges’ time is not spent on “non-adjudicatory” work while India sits '
          'on over five crore pending cases. He also suggested AI predict likely verdicts in cheque-bounce and '
          'money-recovery cases before arguments begin, but said constitutional cases must stay with humans.',
  'why': 'In September, the Supreme Court scrapped a ₹425 crore customs penalty because the order cited judgments that '
         'don’t exist, apparently made up by AI. AI can be “training wheels”, the court said, but not the pilot. The '
         'same goes for any manager signing off on AI work.',
  'sources': [('Bar & Bench',
               'https://www.barandbench.com/news/supreme-court-justice-joymalya-bagchi-bats-for-dedicated-ai-courts-to-decide-mutual-consent-divorce-cases'),
              ('The Week',
               'https://www.theweek.in/news/india/2026/11/21/ai-divorce-courts-proposed-supreme-court-judge.html'),
              ('LiveLaw (₹425 crore penalty)',
               'https://www.livelaw.in/supreme-court/supreme-court-sets-aside-425-crore-penalty-as-customs-authority-used-ai-generated-fake-case-laws-548329')]},
 {'num': '06',
  'tag': 'HEALTHCARE',
  'short': 'AI speeds up drug discovery',
  'headline': 'Big drugmakers say AI has cut drug discovery time by up to half',
  'body': 'Scientists at AstraZeneca, Novartis, Sanofi, Novo Nordisk and others told Reuters on 20 November that AI '
          'has cut the time it takes to design new molecules and move them into clinical trials by up to half this '
          'year. Novartis said its average time from project start to drug candidate is now 18 to 24 months, down from '
          'about three years. Sanofi said it saved at least a year on an asthma drug.',
  'why': 'If this holds, early research gets faster and cheaper, which changes how drugmakers and their investors '
         'value it. But the figures are the companies’ own, and historically nearly nine in ten drugs that enter '
         'clinical trials fail, so faster discovery does not yet mean more medicines.',
  'sources': [('Reuters via Investing.com',
               'https://www.investing.com/news/stock-market-news/big-pharma-with-eye-on-anthropic-says-ai-is-shrinking-drug-discovery-timelines-5041287'),
              ('STAT',
               'https://www.statnews.com/pharmalot/2026/11/20/sanofi-eyeing-insmed-ai-speeding-drug-development/')]},
 {'num': '07',
  'tag': 'SECURITY',
  'short': 'Attacks on Indian lenders',
  'headline': 'Attackers target Indian payment systems and lenders',
  'body': 'Issue 1 reported AI agents reading data inside Indian organisations unnoticed. On 20 November, CERT-In, '
          'India’s cybersecurity agency, warned that attackers were changing payment records and approval chains at '
          'firms handling government-linked payments and vendor payouts, and flagged AI tools that scan for weak '
          'spots. Delhi Police said hackers had diverted more than ₹65 crore of approved loans from at least 12 '
          'non-banking lenders, and found traces of AI use.',
  'why': 'Fraud is moving from tricking customers to quietly editing records inside the systems that approve payments. '
         'The managers who own approval controls and vendor access now carry this risk, not just the IT team.',
  'sources': [('WION (CERT-In)',
               'https://www.wionews.com/technology/ai-agents-now-being-used-by-hackers-to-steal-money-cert-in-issues-warning-1795245429991'),
              ('MediaNama', 'https://www.medianama.com/2026/11/223-ai-hackers-approved-loans-nbfc/'),
              ('Outlook India',
               'https://www.outlookindia.com/national/delhi-ncr-nbfc-cyber-fraud-hackers-rs-65-crore-loan-scam'),
              ('DiSPatch Issue 1', 'https://analyticsclub-spjimr.github.io/newsletters/dispatch/issue-01/')]},
 {'num': '08',
  'tag': 'MARKETING',
  'short': 'Pushback on AI-made ads',
  'headline': 'Indian consumers push back on AI-made ads',
  'body': 'Accenture Song’s Life Trends 2027 survey of more than 28,000 people in 26 countries, released on 18 '
          'November, found that 56% of Indian respondents think brands that use AI for content or ads look “lazy, '
          'careless and cheap”. Worldwide, 60% of 18- to 24-year-olds agreed. Separately, the Advertising Standards '
          'Council of India’s rules on labelling AI-made ads that could mislead, such as those with virtual '
          'influencers, take effect on 29 December.',
  'why': 'Brands using AI to cut production costs risk putting off the young customers they most want, and from late '
         'December an unlabelled AI ad that misleads can draw complaints.',
  'pic': {'label': 'PICTURE FOR THIS STORY',
          'desc': 'Meme: the brand’s AI ad, up close',
          'file': 'images/meme-ai-ads.jpg',
          'alt': 'Two-panel meme. Left, captioned “The brand: Our AI ad looks premium”, a small robot proudly shows a '
                 'glossy perfume ad. Right, captioned “56% of Indians surveyed: Lazy, careless and cheap”, a '
                 'magnifying glass shows the hand in the ad has too many fingers and the label is a blob, and the '
                 'robot looks embarrassed'},
  'sources': [('Accenture',
               'https://newsroom.accenture.com/news/2026/accenture-life-trends-2027-finds-people-want-progress-in-an-ai-era-but-on-their-own-terms'),
              ('The Tribune (ANI)',
               'https://www.tribuneindia.com/news/accenture-report/ai-in-ads-and-content-makes-brands-look-careless-say-56-of-india-respondents-accenture'),
              ('afaqs',
               'https://www.afaqs.com/news/advertising/asci-releases-guidelines-for-responsible-labelling-of-ai-generated-ad-content-12589347'),
              ('Business Standard',
               'https://www.business-standard.com/amp/industry/news/asci-issues-guidelines-for-labelling-synthetically-generated-content-in-ads-126093000414_1.html')]},
 {'num': '09',
  'tag': 'START-UPS',
  'short': 'Sarvam’s rupee-priced AI',
  'headline': 'Sarvam sells India-hosted AI, priced in rupees',
  'body': 'On 16 November, Bengaluru-based Sarvam AI launched Token Factory, which runs Sarvam’s own '
          '105-billion-parameter model and open models such as DeepSeek, Kimi, GLM and Gemma on processors in India, '
          'billed in rupees. DeepSeek V4.1 Flash, for example, costs ₹14 per million input tokens at launch. Critics '
          'asked why a company backed by the IndiaAI Mission was serving mostly Chinese models. Co-founder Pratyush '
          'Kumar said it runs on privately bought processors, not subsidised government computing.',
  'why': 'Keeping data in India and billing in rupees eases two worries for Indian businesses. But leaning on Chinese '
         'open models raises questions of trust and policy that buyers will need to answer.',
  'sources': [('Sarvam AI', 'https://www.sarvam.ai/blogs/sarvam-token-factory'),
              ('The Tribune (ANI)',
               'https://www.tribuneindia.com/news/ai-models/no-government-support-for-running-open-weight-ai-models-says-sarvams-co-founder-amid-chinese-models-row'),
              ('MediaNama', 'https://www.medianama.com/2026/11/223-sarvam-token-factory-india-sovereign-ai/')]},
 {'num': '10',
  'tag': 'CAREERS',
  'short': 'Freshers and AI in Indian IT',
  'headline': 'AI isn’t wiping out India’s IT jobs, but freshers are feeling it',
  'body': 'A Deutsche Bank report released on 19 November calls fears that AI will do to India’s outsourcing jobs what '
          'Chinese factories did to Western manufacturing “overdone”. Tech job openings reached 130,000 in November, '
          'up 27% on a year earlier, according to staffing firm Xpheno. But fresher hiring is slowing, and TCS has '
          '23,460 fewer employees than a year ago. In the US, Goldman Sachs says the feared AI layoff wave did not '
          'arrive this year.',
  'why': 'For MBA graduates, the risk is fewer entry-level openings, not mass layoffs. Deutsche Bank warns that firms '
         'which stop hiring juniors now may run short of senior people later. Roles that pair domain judgement with AI '
         'tools look like the safer bet.',
  'sources': [('ThePrint (Deutsche Bank report)',
               'https://theprint.in/tech/ai-can-trigger-a-china-shock-for-indias-it-sector-but-deutsche-bank-sees-a-silver-lining/3106745/'),
              ('Fortune (Goldman Sachs)',
               'https://fortune.com/2026/11/16/why-no-ai-layoff-wave-goldman-sachs-outlook-recession-jobs/')]},
 {'num': '11',
  'tag': 'TOOLS',
  'short': 'New models from OpenAI and Google',
  'headline': 'OpenAI cuts prices with GPT-6.2 as Google launches Gemini 4 Neon',
  'body': 'OpenAI released GPT-6.2 on 17 November in two versions: Astra, for the hardest work, and Sol, a cheaper '
          'model for everyday tasks. For developers, Astra costs 20% less than GPT-6 Astra. A day later, Google '
          'released Gemini 4 Neon, which sits between its most powerful and fastest models; Google says it ranks first '
          'on Artificial Analysis’s index of AI coding agents.',
  'why': 'The best models keep getting cheaper for the same work. For companies picking AI tools, the cost of getting '
         'a task done now matters as much as which model tops the rankings.',
  'pic': {'label': 'PICTURE FOR THIS STORY',
          'desc': 'Meme: ordering an AI model',
          'file': 'images/meme-model-menu.jpg',
          'alt': 'Meme captioned “Ordering an AI model in November 2026”: a puzzled robot at a café counter looks up '
                 'at a menu of five glowing items labelled Astra, Sol, Neon, Carbon and Hydrogen'},
  'sources': [('OpenAI', 'https://openai.com/index/introducing-gpt-6-2-astra-sol/'),
              ('Google',
               'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/'),
              ('WinBuzzer',
               'https://winbuzzer.com/2026/11/17/gpt-6-2-scores-higher-at-lower-cost-in-ai-tests-xcxwbn/')]}]
