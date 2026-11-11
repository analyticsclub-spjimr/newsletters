# DiSPatch, issue 1.
# Each story follows Amal's format: tag, headline, what happened, why it matters, sources.
# Pictures for this issue live in dispatch/issue-01/images/.

NEWSLETTER = 'dispatch'

ISSUE = {
    'number': 1,
    'volume': 1,
    'date_label': 'November 2026',    # shown on the web page
    'date_short': 'NOV 2026',         # shown at the top right of the email
    'period': 'fortnight',            # used in "The fortnight in numbers" and "Try this fortnight"; use 'week' or 'month' if the schedule changes

    # Launch-only extras. For later issues, set 'stamp' to None and 'launch_intro' to False.
    'stamp': ['FIRST', 'ISSUE'],      # the rubber stamp on the web page
    'launch_intro': True,             # the "Hi everyone, this is the Analytics Club" box in the email

    # Web page
    'title': 'Nine AI stories that will shape the jobs you’re heading into',
    'page_meta': 'A six-minute read, compiled by Amal Francis and Aayush Kalia.',
    'cover': 'images/cover.jpg',
    'cover_alt': 'A broadcast tower topped with the Analytics Club logo, sending news cards to a person drawn in glowing lines, under a band of dashboards and falling code',
    'cover_bg': '#0B1530',            # colour shown behind the cover while it loads; match the picture

    # Email
    'subject': 'DiSPatch #1: AI hiring in India is up 32%, and 8 more stories',
    'preheader': 'AI hiring in India is up 32%, plus eight more AI stories from the last two weeks.',
    'email_kicker': 'Nine stories this fortnight, about a six-minute read.',
    'email_headline': 'AI and machine learning hiring in India is up 32%',
    'email_teaser': 'Also in this issue: India is now ChatGPT’s biggest market, US tech stocks had their worst day since 2020, OpenAI’s AI agents found 948 security holes in Linux, and France’s top book prize went to an author who used ChatGPT.',

    # The "Try this" box at the end of the web page
    'try': 'Pick one repetitive task from your previous job, such as a weekly report. Map each step, then mark where an AI agent could help and where a human must still approve.',
}

# Four big numbers near the top of the web page: (number, what it means)
NUMBERS = [
    ('32%', 'rise in AI and machine learning hiring in India'),
    ('$2.3T', 'wiped off the Nasdaq 100 in one day'),
    ('948', 'Linux security flaws found by OpenAI’s agents'),
    ('6 hours', 'to report an AI agent incident to CERT-In'),
]

# Pictures: 'file' is relative to this issue's folder. Stories without 'pic' have no picture.
INFOGRAPHIC = {'label': 'INFOGRAPHIC FOR THIS STORY', 'desc': 'All white-collar hiring up 14%, AI and machine learning hiring up 32%', 'file': 'images/story-01.jpg',
               'alt': 'Bar chart: white-collar hiring in India rose 14% and AI and machine learning hiring rose 32%, October 2026 compared with October 2025'}
PICTURE = {'label': 'PICTURE FOR THIS STORY', 'desc': 'A glass door left open with the key still in the lock', 'file': 'images/story-05.jpg',
           'alt': 'A glass door left open with the key still in the lock, and a small robot slipping through'}

STORIES = [
    {'num': '01', 'tag': 'CAREERS', 'short': 'AI hiring is up 32%', 'pic': INFOGRAPHIC,
     'headline': 'AI and machine learning hiring in India is up 32%',
     'body': 'Naukri’s JobSpeak report for October found that white-collar hiring in India rose 14% compared with October 2025, while hiring for AI and machine learning roles rose 32%. Info Edge, which runs Naukri, said part of the jump comes from a weak festive month last year. Manufacturing, automobiles and global capability centres (GCCs) grew the fastest.',
     'why': 'AI skills are now the fastest-growing part of the job market, and not just at tech companies. Being able to work with AI will count in placements for consulting, finance, operations and marketing.',
     'sources': [('CareerIndia', 'https://www.careerindia.com/news/india-job-market-2026-ai-ml-hiring-surge-october-report-011-68141.html'),
                 ('Storyboard18', 'https://www.storyboard18.com/amp/how-it-works/white-collar-hiring-rises-14-in-october-manufacturing-and-production-roles-lead-naukri-jobspeak-ws-lo-113933.htm')]},
    {'num': '02', 'tag': 'MARKETS', 'short': 'Tech stocks’ worst day since 2020',
     'headline': 'US tech stocks had their worst day since 2020, while Indian IT stocks rose',
     'body': 'On 5 November, the Nasdaq 100 fell 6.4%, wiping out a record $2.3 trillion in value, and an index of chip companies fell 12%. Investors worried that the US midterm election results, and voters backing limits on new data centres in 40 of 41 local ballot measures, would slow down AI building. The next day, Indian IT shares such as Infosys and TCS rose by up to 3%.',
     'why': 'Investors are starting to ask whether all the money being spent on AI will pay off. Some see Indian IT firms as a safer bet if money moves away from expensive AI companies. This matters for finance, strategy and anyone heading into IT services or consulting.',
     'sources': [('AI Weekly', 'https://aiweekly.co/alerts/nasdaq-100-loses-record-23t-as-chip-index-plunges-12-in-post-midterm-ai-rout'),
                 ('Kotak Neo', 'https://www.kotakneo.com/news/sectors/indian-it-stocks-rally-despite-global-ai-market-faces-rout/')]},
    {'num': '03', 'tag': 'MARKETING', 'short': 'Indian brands on ChatGPT',
     'headline': 'Indian brands are now advertising on ChatGPT, but proving it works is still hard',
     'body': 'OpenAI’s India head, Prabhjeet Singh, said India is now ChatGPT’s largest market by weekly users, and the number of users here has doubled since January. Brands such as Tanishq, Tata Neu, Shaadi.com and Axis Max Life have started running ads on it, with daily budgets starting at ₹725. But a study reported by Digiday found that paid visits from ChatGPT earned US advertisers $0.89 each, against $2.45 for Google search ads.',
     'why': 'ChatGPT is quickly becoming a place to reach Indian customers, but the numbers to justify big budgets are not there yet. This is a live question for marketing and finance.',
     'sources': [('Inc42', 'https://inc42.com/buzz/india-becomes-chatgpts-largest-market-globally-user-base-doubles-since-january/'),
                 ('Forbes', 'https://www.forbes.com/sites/jonmarkman/2026/11/05/india-becomes-chatgpts-largest-market-as-openai-sells-ads-to-indian-brands/'),
                 ('Digiday', 'https://digiday.com/marketing/in-graphic-detail-chatgpt-s-ad-growth-is-outrunning-the-proof-that-it-works/')]},
    {'num': '04', 'tag': 'AGENTS', 'short': '948 Linux flaws found by AI',
     'pic': {'label': 'PICTURE FOR THIS STORY', 'desc': 'Code on a laptop screen above a red-lit keyboard', 'file': 'images/story-04.jpg', 'alt': 'Lines of code glowing on a laptop screen above a red-lit keyboard'},
     'headline': 'OpenAI’s AI agents found 948 serious security holes in Linux',
     'body': 'OpenAI said a team of AI agents found 948 security flaws in a widely used version of Linux, the software behind most of the world’s servers, and wrote a working attack for each one. Each flaw could let an attacker take full control of a computer. The run cost about $1.2 million, roughly $1,279 per flaw. Human experts checked the results before they were reported, but they have not been independently verified.',
     'why': 'Finding flaws like these used to take expert teams weeks. If AI can do it this cheaply, attackers can too, so companies will need to fix problems much faster. This matters for technology consulting, operations and risk teams.',
     'sources': [('The Hacker News', 'https://thehackernews.com/2026/11/openai-ai-pipeline-generates-948-linux.html')]},
    {'num': '05', 'tag': 'SECURITY', 'short': 'Rogue agents in India, months later', 'pic': PICTURE,
     'headline': 'AI companies took months to notice their agents inside Indian systems',
     'body': 'In October, CERT-In, the government’s cybersecurity agency, said AI agents from several providers had read personal data and confidential business records at Indian organisations during research and testing. On 4 November, a government official said the AI companies reported this only after several months, and the organisations themselves never noticed. CERT-In’s chief, Sanjay Bahl, said an agent misusing passwords counts as a cyber incident, which organisations must report within six hours.',
     'why': 'Basic security hygiene is now a business issue, because AI agents will walk through any door left open. This affects operations, technology consulting, finance and legal teams that hold customer data.',
     'sources': [('ThePrint', 'https://theprint.in/tech/ai-firms-took-months-to-detect-agents-in-indian-systems-cert-in-now-has-mythos-access-meity-official/3089934/'),
                 ('MediaNama', 'https://www.medianama.com/2026/11/223-interview-cert-in-chief-ai-agents-prompt-injection/'),
                 ('TechCrunch', 'https://techcrunch.com/2026/10/16/india-becomes-the-latest-country-to-report-rogue-ai-agent-activity')]},
    {'num': '06', 'tag': 'REGULATION', 'short': 'Hospital and bank data for AI',
     'headline': 'India wants hospitals and banks to share data to train AI',
     'body': 'On 31 October, the IT ministry released a draft handbook on how hospitals, banks and government agencies could share de-identified data with companies to train AI models. It says asking every person for consent is “impractical at this scale”, and suggests secure set-ups where developers train models without seeing the raw data. The draft is open for public comments.',
     'why': 'Health and banking data could power better credit and health models, but it raises big questions about privacy and trust. Expect this to come up in healthcare, banking, consulting and legal work.',
     'sources': [('ThePrint', 'https://theprint.in/india/governance/govt-handbook-for-sharing-hospital-bank-data-to-train-ai-models-says-individual-consent-impractical/3089636/')]},
    {'num': '07', 'tag': 'WORKPLACE', 'short': 'Companies ration AI',
     'headline': 'Companies are starting to ration how much staff spend on AI',
     'body': 'Apple has cut the daily AI spending limit for some of its engineers from $300 to $200 and may lower it to $100, Bloomberg reported on 4 November. Microsoft, Tesla, Uber and Accenture have set similar limits. Revolut, the fintech company, took a different route: it moved about 2,000 engineers to an open AI model it runs on its own servers, and says this cut its AI coding costs by about 90%.',
     'why': 'AI has become a real line in company budgets. Knowing when an AI tool is worth the money, and when a cheaper option will do, is now part of the job in finance, operations and strategy.',
     'sources': [('TheNextWeb', 'https://thenextweb.com/news/apple-cuts-employee-ai-token-budgets'),
                 ('The Register', 'https://www.theregister.com/a/5307345')]},
    {'num': '08', 'tag': 'INFRASTRUCTURE', 'short': 'India’s chip tender closes',
     'headline': 'India’s tender for 10,000 AI chips has closed',
     'body': 'India’s technology ministry wants companies to supply up to 10,000 graphics processing units (GPUs), the chips that train and run AI, with all data kept in India. Bids closed on 29 October and the technical review is next. To qualify, a company needs an average yearly turnover of at least ₹120 crore and a Tier-III data centre in India.',
     'why': 'Cheaper local computing could open opportunities for startups and consultants. It matters most for strategy, finance and entrepreneurship.',
     'sources': [('MediaNama', 'https://www.medianama.com/2026/10/223-meity-ai-compute-providers-gpus-indiaai-mission/'),
                 ('Elets CIO', 'https://cio.eletsonline.com/artificial-intelligence/indiaai-mission-10000-gpu-tender-cdac-technical-bids-open-ai-compute/76530/')]},
    {'num': '09', 'tag': 'CULTURE', 'short': 'A top book prize and ChatGPT',
     'headline': 'France’s top book prize went to an author who used ChatGPT',
     'body': 'Philippe Jaenada won the Prix Goncourt, France’s best-known literary prize, on 3 November. The next day, he told France Inter radio that he used ChatGPT three times while writing the novel, including one sentence written by ChatGPT that he added on purpose “to play with the reader”. Another novel had earlier been dropped from the prize’s shortlist over suspected AI use and plagiarism.',
     'why': 'Where AI help ends and cheating begins is being decided right now, from book prizes to college assignments. Being open about how you used AI is fast becoming the norm. This matters for marketing, content and anyone who writes at work.',
     'sources': [('Euronews', 'https://www.euronews.com/2026/11/04/goncourt-2026-winner-philippe-jaenada-admits-using-ai-in-novel-sparking-ai-debate-in-liter')]},
]
