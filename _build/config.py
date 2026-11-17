# Settings shared by every newsletter and every issue.

# Your GitHub Pages address, ending with /. For example: 'https://yourname.github.io/newsletters/'
# Fill this in once the repo is live. It lets WhatsApp and LinkedIn show the cover picture when someone shares a link.
SITE_URL = 'https://analyticsclub-spjimr.github.io/newsletters/'

CLUB = 'Analytics Club'
SCHOOL_SHORT = 'SPJIMR'
SCHOOL_FULL = 'S. P. Jain Institute of Management & Research'

LINKEDIN = 'https://www.linkedin.com/company/analytics-club-spjimr/posts/'
INSTAGRAM = 'https://www.instagram.com/analyticsclub_spjimr'

# The three newsletters, in the order they appear on the front page.
# 'parts' splits each name so the SP in the middle can be coloured.
# 'status' is 'live' once the first issue is out, otherwise 'soon'.
NEWSLETTERS = [
    {'id': 'dispatch', 'name': 'DiSPatch', 'parts': ('Di', 'SP', 'atch'), 'accent': '#C8361F',
     'tagline': 'AI news, every two weeks.',
     'about': 'The latest AI news, every two weeks.',
     'status': 'live'},
    {'id': 'perspective', 'name': 'PerSPective', 'parts': ('Per', 'SP', 'ective'), 'accent': '#2149C9',
     'tagline': 'AI through the lens of every field.',
     'about': 'How AI is mixing with different fields, like marketing, finance, operations and more.',
     'status': 'live',
     # PerSPective uses a cool blue palette instead of DiSPatch's warm one: {old colour: new colour}
     'theme': {'#F7ECE8': '#EDF1F8', '#ECE4DF': '#DCE3EF', '#E8DCD5': '#D6DEEC', '#A82A16': '#1A3AA8',
               '#FCEDEA': '#E6ECFA', '#FF8A70': '#8FB0FF', '#FDF5F2': '#F1F5FC', '#F2DDD6': '#D9E2F2',
               '#F4C7BE': '#B9C9F2'}},
    {'id': 'grasp', 'name': 'GraSP', 'parts': ('Gra', 'SP', ''), 'accent': '#B98100',
     'tagline': 'One AI concept at a time.',
     'about': 'One AI concept at a time, taught simply.',
     'status': 'soon'},
]
