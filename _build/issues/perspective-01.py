# PerSPective, issue 1: AI x Marketing, by Srihari.
# The article text is the writer's own; only paragraph breaks were added for reading on a phone.
# Pictures for this issue live in perspective/issue-01/images/.

NEWSLETTER = 'perspective'

ISSUE = {
    'number': 1,
    'volume': 1,
    'date_label': 'Sunday 22 November 2026',   # shown on the web page
    'date_short': '22 NOV 2026',               # shown at the top right of the email
    'stamp': ['FIRST', 'ISSUE'],               # rubber stamp on the web page; None for later issues

    # Web page
    'kicker': 'AI × MARKETING',
    'title': 'Half your ad money is wasted. AI now knows which half.',
    'page_meta': 'A four-minute read by Srihari.',
    'cover': 'images/cover.jpg',
    'cover_alt': 'A person drawn in glowing blue lines looks through a magnifying lens; inside it, a shopping street turns into ad cards, charts and a customer path',
    'cover_bg': '#0B1530',
    'reply_big': 'Which field should PerSPective look at next?',
    'reply_small': 'Reply to the PerSPective mail and tell us.',

    # Email
    'subject': 'PerSPective #1: Half your ad money is wasted. AI now knows which half.',
    'preheader': 'AI × Marketing, by Srihari. A four-minute read for your Sunday.',
    'intro_text': 'This is the first PerSPective. Every other Sunday, someone from the batch picks one field and looks at what AI is really changing there. We’re starting with marketing.',
    'email_kicker': 'AI × Marketing, a four-minute read',
    'email_headline': 'Half your ad money is wasted. AI now knows which half.',
    'email_teaser': 'A 19th-century retailer famously said half his advertising was wasted, he just didn’t know which half. Today a model can tell you, down to the ad set and the hour. Srihari looks at what that changes for marketers, and what happens when the algorithm runs the brand voice on its own.',
    'email_byline': 'Written by Srihari',
    'button': 'Read the article',
    'email_reply_small': 'Reply to this mail and tell us.',
}

# The article, block by block:
#   ('p', text)                  a paragraph
#   ('quote', text, who)         a pull quote
#   ('point', '01', lead, text)  a numbered point
#   ('h2', text)                 a section heading
#   ('fig', file, alt, caption)  a picture
#   ('end', text)                the closing line, in a box
BODY = [
    ('p', 'Picture this, you wake up one morning, stretch and reach for your phone and open the first news article you see. It is about the same old AI in the workplace feed and it tells you for the umpteenth time on how AI is taking over the workplace again, which is causing layoffs. Not this again you groan and scroll up and see an ad for a toothpaste. Hmmm, suspicious you think at this time of the day and immediately after you wake up. But this is the least what AI can do in digital marketing nowadays.'),
    ('p', 'No matter how varied the opinion is on AI these days, with some people swearing by it, that it makes their lives easier, while others seem to have enough of it and see it as a massive word prediction software, (myself being in the latter), there is no doubt about the advancements it has achieved in everyday life and industry, one such space being digital marketing.'),
    ('quote', '“Half the money I spend on advertising is wasted; the trouble is I don’t know which half.”', 'Attributed to John Wanamaker, the 19th-century retail titan'),
    ('p', 'If John were alive today and walking through the quad after a brutal Marketing Management case prep, an ensemble gradient-boosted model would tap him on the shoulder, hand him a dashboard, and say: “Actually, John, it was precisely 48.7% of ad set B on Tuesday at 2:14 AM. Also, your creative fatigued three days ago.”'),
    ('fig', 'images/wasted-half.jpg', 'A glowing pie chart split in two: one half sends ad cards to a person, the other half breaks apart, with a magnifying lens on the line between them', 'The wasted half, finally visible.'),
    ('p', 'Welcome to modern digital marketing, where gut feelings and apparent natural creativity are trumped by neural networks, and the intersection with AI looks less like a neat Venn diagram and more like a high-speed collision inside a Snowflake warehouse.'),
    ('p', 'Enter machine learning. The goal is no longer just tracking where a user went yesterday; it is predicting where their intent will land tomorrow. Marketing analytics has shifted from descriptive post-mortems (“Why did nobody buy our farm fresh milk?”) to prescriptive dynamic interventions:'),
    ('point', '01', 'Multi-touch attribution without the hallucinations', 'Traditional last-touch attribution gave 100% of the credit to the final search ad, ignoring the podcast mention, the YouTube pre-roll, and the three weeks of subconscious brand conditioning. Bayesian attribution models and Shapley-value formulations now weigh the true incremental lift of every channel touchpoint before marketing budgets are incinerated.'),
    ('fig', 'images/attribution.jpg', 'A customer path through a podcast, a video ad, a phone and a search bar to a shopping bag, with a bar under each step showing its share of the credit', 'Every step of the journey gets its fair share of the credit, not just the last click.'),
    ('point', '02', 'Hyper-personalization at scale', 'We’ve graduated from “Hello {First_Name}” email marketing. GenAI and reinforcement learning loops now tailor value propositions on the fly. A price-sensitive student studying near Andheri gets ad copy highlighting bundle discounts and immediate delivery, while an impulse buyer gets scarcity framing, rendered in real-time by dynamic creative optimization (DCO) engines.'),
    ('point', '03', 'Synthetic personas and pre-testing', 'Why blow millions on a nationwide focus group when you can prompt fine-tuned agentic clusters that simulate your demographic cohorts? Marketers are running synthetic testing rounds on copy, sentiment, and visual assets before spending their first media dollar.'),
    ('fig', 'images/black-box.jpg', 'A glowing black box spits out loud, chaotic ad cards on one side, while a human hand on a slider turns its output into calm, orderly cards on the other', 'An algorithm optimises for exactly what you ask. The guardrails are your job.'),
    ('h2', 'The “black box” dilemma (or, when the AI goes rogue)'),
    ('p', 'Of course, letting neural networks run your brand voice is a bit like handing a flamethrower to an over-enthusiastic MBA intern who is over caffeinated and simultaneously hungry to prove themselves.'),
    ('p', 'Algorithms optimize strictly for the loss function you hand them. If you tell an engine to maximize clicks without guardrails, it will gladly write clickbait so sensational that your premium B2B SaaS platform begins to look like a tabloid exposé on the Bollywood party culture. Furthermore, algorithmic bias and data drift mean that what drove conversions during Diwali might crash your ROAS completely by February.'),
    ('p', 'Marketing effectiveness requires equal parts Python script and behavioral economics. The data tells you what happened down to the millisecond; human intuition and brand strategy tell you why a customer cared enough to click.'),
    ('h2', 'What it means for the next generation of managers'),
    ('p', 'If you think marketing in the AI era means sitting back while prompt generators run your agency on autopilot, you’re looking at the wrong half of the dashboard. The brands winning today aren’t the ones spamming automated content; they’re the ones building closed-loop data pipelines, understanding customer lifetime value (LTV) anomalies, and treating every campaign like a live statistical hypothesis.'),
    ('end', 'The algorithm has solved the targeting puzzle. The next challenge is making sure the message is actually worth reading.'),
]
