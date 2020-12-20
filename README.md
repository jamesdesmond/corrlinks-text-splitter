**This project is hosted online at my website [HERE](http://jamesdesmond.org/posts/corrlinks-text-split/)**

# Corrlinks Text Splitter

I created this script because I have been involved in a program called [Donate Your Vote](https://emancipationinitiative.org/get-involved/donateyourvote-2020/)

I typically use email to communicate with my penpal at [MCI-Norfolk](https://www.mass.gov/locations/mci-norfolk). Inmates are not allowed typical email access. A service, Corrlinks, provides an emai like service, for a per-email fee.
Corrlinks also has a maximum character and line limit. 

Corrlinks charges $0.25 for each email sent by a person on the outside, or inside.
- Character cap: 13000 characters (including newlines)
- Line cap: 100 lines

Frequently my replies would go well over the line and character maximums, which would cause me to then need to manually slice my messages to fit.

I saw an opportunity to script, and took it.

# Prereqs
- Python 3.7 minimum
- Pip

# Installation

`pip install -r requirements.txt`

# Running the script

`python3 src\corrlinks-text-splitter` (_in root repo directory_)

# Output

Output will be in separate text files in `corrlinks-text-splitter\output\`